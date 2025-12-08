#!/usr/bin/env python3
"""
YouTube Auto-Upload Script
Automatically uploads all framework videos to YouTube Shorts
Uses YouTube Data API v3

Setup:
1. Install: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
2. Get OAuth credentials from: https://console.cloud.google.com/
3. Download client_secrets.json to this directory
4. Run script - it will authenticate via browser

Usage:
python3 youtube_auto_upload.py
"""

import os
import sys
from pathlib import Path
import json

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    import pickle
except ImportError:
    print("❌ Missing dependencies. Install with:")
    print("pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# Video metadata for each framework
VIDEO_METADATA = {
    'TCREI_FAST_FINAL.mp4': {
        'title': 'TCREI: Perfect AI Alignment Framework #Shorts',
        'description': '''Stop letting AI guess what you want!

TCREI = Perfect AI alignment:
T - Task: Define specific goals
C - Context: Share why it matters
R - Resources: Provide examples
E - Evaluation: Measure success
I - Iteration: Refine through feedback

🔗 Try the RPI Framework:
github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #AI #Programming #TCREI #DevTips #MachineLearning #CodeBetter''',
        'tags': ['shorts', 'ai', 'programming', 'tcrei', 'framework', 'coding', 'developer', 'tech'],
        'category': '28'  # Science & Technology
    },
    'STAR_METHOD_FINAL.mp4': {
        'title': 'STAR Method: Ace Your Behavioral Interviews #Shorts',
        'description': '''Master behavioral interviews with STAR!

S - Situation: Describe the context
T - Task: Explain the challenge
A - Action: Detail your steps
R - Result: Share the outcome

Perfect for job interviews, performance reviews, and storytelling.

🔗 More frameworks:
github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Interview #Career #STAR #JobInterview #BehavioralInterview #CareerTips''',
        'tags': ['shorts', 'interview', 'career', 'star method', 'job interview', 'behavioral interview'],
        'category': '27'  # Education
    },
    'SMART_GOALS_FINAL.mp4': {
        'title': 'SMART Goals: Set Better Goals Every Time #Shorts',
        'description': '''Stop setting vague goals. Use SMART!

S - Specific: Clear objectives
M - Measurable: Track metrics
A - Achievable: Realistic targets
R - Relevant: Aligned vision
T - Time-bound: Set deadlines

Transform your goal-setting today.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Goals #Productivity #SMART #GoalSetting #Success #SelfImprovement''',
        'tags': ['shorts', 'goals', 'productivity', 'smart goals', 'self improvement', 'success'],
        'category': '27'
    },
    'RICE_FINAL.mp4': {
        'title': 'RICE Framework: Prioritize Features Like a Pro #Shorts',
        'description': '''Prioritize features using RICE scoring!

R - Reach: How many users?
I - Impact: Effect per person?
C - Confidence: How sure?
E - Effort: Work required?

Score = (R × I × C) / E

Perfect for product managers and developers.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #ProductManagement #RICE #Prioritization #ProductDev #PM''',
        'tags': ['shorts', 'product management', 'rice', 'prioritization', 'product development'],
        'category': '28'
    },
    'CIA_FINAL.mp4': {
        'title': 'CIA Triad: The Foundation of Cybersecurity #Shorts',
        'description': '''Every security strategy needs CIA!

C - Confidentiality: Keep data private
I - Integrity: Maintain accuracy
A - Availability: Ensure access

The three pillars of information security.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Cybersecurity #CIA #InfoSec #Security #DataProtection #CyberSecurity''',
        'tags': ['shorts', 'cybersecurity', 'cia triad', 'infosec', 'security', 'data protection'],
        'category': '28'
    },
    'SOLID_FINAL.mp4': {
        'title': 'SOLID Principles: Write Clean OOP Code #Shorts',
        'description': '''Master object-oriented design with SOLID!

S - Single Responsibility
O - Open-Closed
L - Liskov Substitution
I - Interface Segregation
D - Dependency Inversion

Write better, maintainable code.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Programming #SOLID #OOP #CleanCode #SoftwareEngineering #Coding''',
        'tags': ['shorts', 'programming', 'solid', 'oop', 'clean code', 'software engineering'],
        'category': '28'
    },
    'MECE_FINAL.mp4': {
        'title': 'MECE: Structure Any Problem Perfectly #Shorts',
        'description': '''McKinsey's secret weapon: MECE!

M - Mutually: No overlap
E - Exclusive: One category each
C - Collectively: Cover everything
E - Exhaustive: Nothing left out

Perfect problem decomposition.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #ProblemSolving #MECE #Consulting #Strategy #McKinsey #Frameworks''',
        'tags': ['shorts', 'problem solving', 'mece', 'consulting', 'strategy', 'mckinsey'],
        'category': '27'
    },
    'AIDA_FINAL.mp4': {
        'title': 'AIDA Model: Convert Like a Marketing Pro #Shorts',
        'description': '''Classic marketing framework that works!

A - Attention: Grab them
I - Interest: Build value
D - Desire: Create want
A - Action: Drive CTA

Perfect for copywriting and campaigns.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Marketing #AIDA #Copywriting #Sales #MarketingTips #Advertising''',
        'tags': ['shorts', 'marketing', 'aida', 'copywriting', 'sales', 'advertising'],
        'category': '27'
    },
    'OODA_FINAL.mp4': {
        'title': 'OODA Loop: Make Faster Decisions #Shorts',
        'description': '''Military strategy for rapid decisions!

O - Observe: Gather info
O - Orient: Analyze context
D - Decide: Choose action
A - Act: Execute & iterate

Speed wins. OODA faster.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #Strategy #OODA #DecisionMaking #Military #Leadership #Tactics''',
        'tags': ['shorts', 'strategy', 'ooda loop', 'decision making', 'military', 'leadership'],
        'category': '27'
    },
    'RACI_FINAL.mp4': {
        'title': 'RACI Matrix: Clarify Team Roles Instantly #Shorts',
        'description': '''Stop role confusion with RACI!

R - Responsible: Does work
A - Accountable: Final authority
C - Consulted: Provides input
I - Informed: Gets updates

Clear roles = better teams.

🔗 github.com/drewbeyersdorf/agent-improvement-techniques

#Shorts #ProjectManagement #RACI #Teamwork #Leadership #Management #PM''',
        'tags': ['shorts', 'project management', 'raci', 'teamwork', 'leadership', 'management'],
        'category': '27'
    }
}


def get_authenticated_service():
    """Authenticate with YouTube API"""
    creds = None
    token_file = 'youtube_token.pickle'

    # Load existing credentials
    if os.path.exists(token_file):
        print("📂 Loading saved credentials...")
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # Refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Refreshing credentials...")
            creds.refresh(Request())
        else:
            if not os.path.exists('client_secrets.json'):
                print("\n❌ ERROR: client_secrets.json not found!")
                print("\nHow to get it:")
                print("1. Go to: https://console.cloud.google.com/")
                print("2. Create a project (or select existing)")
                print("3. Enable YouTube Data API v3")
                print("4. Create OAuth 2.0 Client ID credentials")
                print("5. Download as client_secrets.json")
                print("6. Place in this directory")
                print("\nThen run this script again.")
                sys.exit(1)

            print("🔐 Authenticating... (browser will open)")
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials
        print("💾 Saving credentials...")
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    print("✅ Authentication successful!")
    return build('youtube', 'v3', credentials=creds)


def upload_video(youtube, video_path, metadata):
    """Upload a single video to YouTube"""
    filename = Path(video_path).name
    print(f"\n{'='*70}")
    print(f"📤 Uploading: {filename}")
    print(f"{'='*70}")

    body = {
        'snippet': {
            'title': metadata['title'],
            'description': metadata['description'],
            'tags': metadata['tags'],
            'categoryId': metadata['category']
        },
        'status': {
            'privacyStatus': 'public',  # Change to 'private' or 'unlisted' if needed
            'selfDeclaredMadeForKids': False,
        }
    }

    # Create media upload
    media = MediaFileUpload(
        video_path,
        mimetype='video/mp4',
        resumable=True,
        chunksize=1024*1024  # 1MB chunks
    )

    # Execute upload
    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    print(f"📊 Title: {metadata['title']}")
    print(f"⏳ Uploading...")

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            progress = int(status.progress() * 100)
            print(f"  Progress: {progress}%", end='\r')

    print(f"\n✅ Uploaded successfully!")
    print(f"🔗 Video ID: {response['id']}")
    print(f"🔗 URL: https://youtube.com/shorts/{response['id']}")

    return response


def upload_all_videos():
    """Upload all framework videos"""
    print("\n" + "="*70)
    print("🎬 YOUTUBE AUTO-UPLOAD")
    print("Uploading all framework videos to YouTube Shorts")
    print("="*70 + "\n")

    # Authenticate
    youtube = get_authenticated_service()

    # Find videos
    video_paths = []

    # TCREI video
    tcrei_path = Path('../../output/tcrei_short/TCREI_FAST_FINAL.mp4')
    if tcrei_path.exists():
        video_paths.append(tcrei_path)

    # Framework videos
    for video_file in VIDEO_METADATA.keys():
        if video_file != 'TCREI_FAST_FINAL.mp4':
            path = Path(f'../../output/framework_shorts/{video_file}')
            if path.exists():
                video_paths.append(path)

    if not video_paths:
        print("❌ No videos found!")
        return

    print(f"📹 Found {len(video_paths)} videos to upload\n")

    # Upload each video
    uploaded = []
    for video_path in video_paths:
        filename = video_path.name
        if filename in VIDEO_METADATA:
            try:
                response = upload_video(youtube, str(video_path), VIDEO_METADATA[filename])
                uploaded.append({
                    'filename': filename,
                    'video_id': response['id'],
                    'url': f"https://youtube.com/shorts/{response['id']}"
                })
            except Exception as e:
                print(f"❌ Error uploading {filename}: {e}")
        else:
            print(f"⚠️  No metadata for {filename}, skipping...")

    # Summary
    print("\n" + "="*70)
    print(f"✅ UPLOAD COMPLETE! ({len(uploaded)}/{len(video_paths)} videos)")
    print("="*70 + "\n")

    if uploaded:
        print("📺 Uploaded videos:\n")
        for video in uploaded:
            print(f"  ✅ {video['filename']}")
            print(f"     {video['url']}\n")

        # Save URLs to file
        with open('uploaded_videos.txt', 'w') as f:
            for video in uploaded:
                f.write(f"{video['filename']}: {video['url']}\n")

        print("💾 URLs saved to: uploaded_videos.txt")

    print("\n🎉 All done! Your videos are live on YouTube Shorts!")


if __name__ == '__main__':
    upload_all_videos()
