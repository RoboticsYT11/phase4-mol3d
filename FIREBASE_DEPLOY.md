# Deploy Phase4-Mol3D to Firebase

## ⚠️ Important Note
Firebase Cloud Functions with Python + RDKit can be **expensive** and **slow** compared to other platforms. Consider using **Render** or **Railway** instead for better performance and cost.

## Prerequisites

1. **Install Firebase CLI**:
   ```bash
   npm install -g firebase-tools
   ```

2. **Install Node.js** (required for Firebase CLI)

## Deployment Steps

### Step 1: Firebase Setup
```bash
# Login to Firebase
firebase login

# Initialize Firebase in your project
cd phase4-mol3d
firebase init

# Select:
# - Functions (Python)
# - Hosting
# - Use existing project or create new one
```

### Step 2: Deploy
```bash
# Deploy everything
firebase deploy

# Or deploy separately:
firebase deploy --only functions
firebase deploy --only hosting
```

### Step 3: Get Your URL
After deployment, Firebase will give you:
- **Hosting URL**: `https://your-project.web.app`
- **Functions URL**: `https://us-central1-your-project.cloudfunctions.net/api`

## Alternative: Hybrid Approach (Recommended)

Deploy frontend on Firebase, backend elsewhere:

1. **Frontend on Firebase**:
   ```bash
   firebase deploy --only hosting
   ```

2. **Backend on Render/Railway**:
   - Deploy your Flask app to Render (free)
   - Update API URLs in `public/index.html` to point to your Render URL

## Cost Warning ⚠️

Firebase Cloud Functions charges for:
- **Invocations**: $0.40 per million
- **Compute time**: $0.0000025 per 100ms
- **Memory**: Additional costs for high memory usage

RDKit molecular calculations can be memory/CPU intensive, making this expensive for heavy usage.

## Recommended Alternative

Use **Render** instead:
1. Free tier available
2. Better suited for Python/RDKit
3. Simpler deployment
4. No per-invocation costs

Deploy command for Render:
```bash
git push origin main  # Push to GitHub
# Then deploy on render.com
```