# 📺 YouTube Auto-Upload Setup Guide

This guide will help you automatically upload all 10 framework videos to YouTube Shorts.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies (1 minute)

```bash
pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 2: Get YouTube API Credentials (5 minutes)

1. **Go to Google Cloud Console**:
   - Visit: https://console.cloud.google.com/

2. **Create a Project** (or select existing):
   - Click "Select a Project" → "New Project"
   - Name it: "YouTube Framework Uploads"
   - Click "Create"

3. **Enable YouTube Data API v3**:
   - In the search bar, type "YouTube Data API v3"
   - Click on it → Click "Enable"

4. **Create OAuth 2.0 Credentials**:
   - Go to: APIs & Services → Credentials
   - Click "+ CREATE CREDENTIALS" → "OAuth client ID"
   - If prompted, configure OAuth consent screen:
     - User Type: External
     - App name: "Framework Videos"
     - User support email: your email
     - Developer contact: your email
     - Click "Save and Continue"
     - Scopes: Skip (click "Save and Continue")
     - Test users: Add your Google account email
     - Click "Save and Continue"
   - Back to "Create OAuth client ID":
     - Application type: **Desktop app**
     - Name: "YouTube Upload Script"
     - Click "Create"

5. **Download Credentials**:
   - Click the download icon (⬇️) next to your newly created OAuth client
   - This downloads a JSON file
   - **Rename it to**: `client_secrets.json`
   - **Move it to**: `/Users/methodologydevelopmenthq/Desktop/RPI_Framework_Package/`

### Step 3: Run Auto-Upload (2 minutes)

```bash
cd /Users/methodologydevelopmenthq/Desktop/RPI_Framework_Package
python3 youtube_auto_upload.py
```

**What happens**:
1. Browser opens for you to sign in to Google
2. Approve the app to upload videos
3. Script automatically uploads all 10 videos
4. Each video gets proper title, description, tags, and GitHub link
5. URLs saved to `uploaded_videos.txt`

---

## 📋 What Gets Uploaded

All 10 videos with optimized metadata:

1. **TCREI** - AI Alignment Framework
2. **STAR Method** - Behavioral Interviews
3. **SMART Goals** - Goal Setting
4. **RICE Framework** - Feature Prioritization
5. **CIA Triad** - Cybersecurity
6. **SOLID Principles** - OOP Design
7. **MECE Method** - Problem Structuring
8. **AIDA Model** - Marketing
9. **OODA Loop** - Decision Making
10. **RACI Matrix** - Role Clarity

Each video includes:
- ✅ Optimized title with #Shorts hashtag
- ✅ Detailed description
- ✅ Relevant tags for discovery
- ✅ GitHub link to your repo
- ✅ Proper category (Education or Science & Technology)

---

## 🎯 Privacy Settings

By default, videos are uploaded as **PUBLIC**.

To change this, edit `youtube_auto_upload.py` line ~287:

```python
'privacyStatus': 'public',  # Change to 'private' or 'unlisted'
```

Options:
- `'public'` - Anyone can find and watch
- `'unlisted'` - Only people with the link can watch
- `'private'` - Only you can watch

---

## 🔧 Customization

### Change Titles/Descriptions

Edit the `VIDEO_METADATA` dictionary in `youtube_auto_upload.py` (starting at line ~33).

Example:
```python
'TCREI_FAST_FINAL.mp4': {
    'title': 'Your Custom Title #Shorts',
    'description': 'Your custom description...',
    'tags': ['your', 'tags', 'here'],
    'category': '28'  # 28=Science & Tech, 27=Education
}
```

### Upload Specific Videos Only

Comment out videos you don't want in the `VIDEO_METADATA` dictionary.

---

## 📊 After Upload

The script creates `uploaded_videos.txt` with all YouTube Shorts URLs:

```
TCREI_FAST_FINAL.mp4: https://youtube.com/shorts/ABC123
STAR_METHOD_FINAL.mp4: https://youtube.com/shorts/DEF456
...
```

You can share these links on:
- Twitter/X
- LinkedIn
- Reddit (r/programming, r/productivity, r/cscareerquestions)
- Dev.to
- Hacker News

---

## ⚠️ Troubleshooting

### Error: "client_secrets.json not found"
- Download OAuth credentials from Google Cloud Console
- Rename to exactly `client_secrets.json`
- Place in the same folder as `youtube_auto_upload.py`

### Error: "Access blocked: Authorization Error"
- In Google Cloud Console, add your email to "Test users" in OAuth consent screen
- Make sure YouTube Data API v3 is enabled

### Error: "The request cannot be completed because you have exceeded your quota"
- YouTube API has daily quota limits
- Default: 10,000 units/day
- Each upload: ~1,600 units
- You can upload ~6 videos per day
- Wait 24 hours or request quota increase

### Browser doesn't open for authentication
- Manually visit the URL shown in terminal
- Sign in and approve
- Copy the authorization code back to terminal

---

## 🎉 Tips for Maximum Reach

After uploading:

1. **Pin a comment** on each video linking to your GitHub
2. **Add to playlists**: Create a "Frameworks" playlist
3. **Cross-post**: Share on TikTok, Instagram Reels
4. **Engage**: Respond to every comment in first 24 hours
5. **Schedule**: Upload 1-2 per day for consistent algorithm boost

---

## 🔒 Security Notes

- `client_secrets.json` - Keep private (contains OAuth client ID)
- `youtube_token.pickle` - Keep private (contains your access token)
- Add to `.gitignore` if using Git:
  ```
  client_secrets.json
  youtube_token.pickle
  ```

---

## 📚 Resources

- YouTube Data API Docs: https://developers.google.com/youtube/v3
- OAuth 2.0 Guide: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps
- Quota Calculator: https://developers.google.com/youtube/v3/determine_quota_cost

---

**Ready to upload? Run:**
```bash
python3 youtube_auto_upload.py
```

🎬 Let's teach the world about frameworks! 🚀
