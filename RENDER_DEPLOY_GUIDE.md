# 🚀 Deploy Phase4-Mol3D to Render - Step by Step

## Step 1: Create GitHub Repository

1. **Go to GitHub.com** and sign in (create account if needed)
2. **Click "New Repository"**
   - Repository name: `phase4-mol3d`
   - Make it Public
   - Don't initialize with README
   - Click "Create repository"

## Step 2: Push Your Code to GitHub

Open Command Prompt in your project folder and run:

```bash
# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/phase4-mol3d.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Deploy on Render

1. **Go to [render.com](https://render.com)**
2. **Sign up for free** (use GitHub account for easy connection)
3. **Click "New +" → "Web Service"**
4. **Connect GitHub** and select your `phase4-mol3d` repository
5. **Configure deployment**:
   - **Name**: `phase4-mol3d` (or any name you like)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`
6. **Click "Create Web Service"**

## Step 4: Wait for Deployment

- Render will automatically build and deploy your app
- This takes 5-10 minutes for first deployment
- You'll get a live URL like: `https://phase4-mol3d-xyz.onrender.com`

## Step 5: Access Your App

Your molecular visualization app will be live and accessible to anyone worldwide!

## 🎉 That's it! 

Your app includes:
- ✅ 3D molecular visualization
- ✅ Hand gesture controls
- ✅ SMILES to 3D conversion
- ✅ PDB protein loading
- ✅ Predefined molecule library

## Troubleshooting

If deployment fails:
1. Check the build logs in Render dashboard
2. Ensure all files are pushed to GitHub
3. Verify requirements.txt has correct dependencies

## Free Tier Limitations

- App may sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up
- Upgrade to paid plan ($7/month) for always-on service