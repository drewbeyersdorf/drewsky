#!/bin/bash
# Batch generator for all 10 framework videos
# Run with: bash create_all_frameworks.sh

echo "🎬 FRAMEWORK VIDEO BATCH GENERATOR"
echo "Creating 10 B&W classical framework videos..."
echo ""

# Already created:
echo "✅ 1. TCREI (already created)"
echo "✅ 2. STAR Method (already created)"
echo "✅ 3. SMART Goals (already created)"
echo ""

# Generate remaining 7:
echo "🎬 Generating remaining frameworks..."
echo ""

# 3. RICE Framework
echo "📊 Creating RICE Framework..."
python3 create_rice_video.py

# 4. CIA Triad
echo "🔒 Creating CIA Triad..."
python3 create_cia_video.py

# 5. SOLID Principles
echo "💻 Creating SOLID Principles..."
python3 create_solid_video.py

# 6. MECE Method
echo "📐 Creating MECE Method..."
python3 create_mece_video.py

# 7. AIDA Model
echo "📢 Creating AIDA Model..."
python3 create_aida_video.py

# 8. OODA Loop
echo "⚡ Creating OODA Loop..."
python3 create_ooda_video.py

# 9. RACI Matrix
echo "👥 Creating RACI Matrix..."
python3 create_raci_video.py

echo ""
echo "="*70
echo "✅ ALL FRAMEWORK VIDEOS COMPLETE!"
echo "📁 Location: ../../output/framework_shorts/"
echo "="*70
echo ""

ls -lh ../../output/framework_shorts/*_FINAL.mp4

echo ""
echo "🎉 Ready to upload to YouTube Shorts, TikTok, Instagram Reels!"
