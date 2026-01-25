# TikTok Shop Radar - Deployment Guide

## 🚀 Free Hosting Options with Custom Domain Support

### Option 1: **Railway.app** (Recommended ⭐)
- **Free tier**: $5 credit/month (enough for small apps)
- **Custom domain**: ✅ Free
- **Database**: PostgreSQL included
- **Deploy time**: ~5 minutes

#### Railway Deployment Steps:

1. **Push to GitHub**
   ```bash
   cd /home/devlight/Desktop/tiktokshopradar
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   # Create a new repo on GitHub, then:
   git remote add origin https://github.com/YOUR_USERNAME/tiktokshopradar.git
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `tiktokshopradar` repository
   - Railway will auto-detect Django

3. **Add PostgreSQL Database**
   - In your project, click "+ New"
   - Select "Database" → "Add PostgreSQL"
   - Railway auto-connects it via `DATABASE_URL`

4. **Set Environment Variables**
   Click on your Django service → Variables tab:
   ```
   SECRET_KEY=your-generated-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,*.railway.app
   ```

5. **Generate SECRET_KEY**
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

6. **Connect Custom Domain**
   - Go to Settings → Domains
   - Click "Custom Domain"
   - Enter your domain: `yourdomain.com`
   - Add the CNAME record to your domain registrar:
     ```
     Type: CNAME
     Name: @ (or www)
     Value: [shown by Railway]
     ```

---

### Option 2: **Render.com**
- **Free tier**: Yes (with limitations)
- **Custom domain**: ✅ Free
- **Database**: PostgreSQL free tier available
- **Deploy time**: ~10 minutes

#### Render Deployment Steps:

1. **Push to GitHub** (same as above)

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repo

3. **Configure Web Service**
   ```
   Name: tiktokshopradar
   Environment: Python 3
   Build Command: ./build.sh
   Start Command: gunicorn tiktokshopradar.wsgi:application
   ```

4. **Add PostgreSQL**
   - Click "New +" → "PostgreSQL"
   - Select Free tier
   - Copy the Internal Database URL

5. **Set Environment Variables**
   In your web service → Environment:
   ```
   SECRET_KEY=[generated key]
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,*.onrender.com
   DATABASE_URL=[your postgres internal URL]
   ```

6. **Connect Custom Domain**
   - Go to Settings → Custom Domains
   - Add your domain
   - Update DNS with provided CNAME

---

### Option 3: **Fly.io**
- **Free tier**: 3 shared VMs free
- **Custom domain**: ✅ Free
- **Database**: Requires separate setup
- **Deploy time**: ~15 minutes

#### Fly.io Deployment Steps:

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Initialize and Deploy**
   ```bash
   cd /home/devlight/Desktop/tiktokshopradar
   fly auth login
   fly launch
   ```

3. **Add PostgreSQL**
   ```bash
   fly postgres create
   fly postgres attach [your-postgres-app]
   ```

4. **Set Secrets**
   ```bash
   fly secrets set SECRET_KEY="your-secret-key"
   fly secrets set DEBUG=False
   fly secrets set ALLOWED_HOSTS="yourdomain.com,*.fly.dev"
   ```

5. **Deploy**
   ```bash
   fly deploy
   ```

6. **Add Custom Domain**
   ```bash
   fly certs add yourdomain.com
   ```

---

### Option 4: **PythonAnywhere**
- **Free tier**: Yes (limited)
- **Custom domain**: ❌ Paid only ($5/month)
- **Database**: MySQL/PostgreSQL
- **Deploy time**: ~20 minutes
- **Note**: Best for Django but custom domain not free

---

## 🎯 Recommended: Railway.app

**Why Railway?**
- Easiest setup for Django
- Free custom domain support
- Auto-detects Django projects
- Built-in PostgreSQL
- Generous free tier ($5/month credit)
- Zero-config deployments

---

## 📋 Pre-Deployment Checklist

✅ Files created:
- `requirements.txt` (with gunicorn, whitenoise, etc.)
- `Procfile` (for process management)
- `runtime.txt` (Python version)
- `build.sh` (build script)
- `.env.example` (environment template)
- Updated `settings.py` (production-ready)

✅ Next steps:
1. Choose hosting platform (Railway recommended)
2. Push code to GitHub
3. Deploy on platform
4. Add PostgreSQL database
5. Set environment variables
6. Connect your custom domain

---

## 🔐 Security Reminders

- Never commit `.env` file (it's in `.gitignore`)
- Generate a strong `SECRET_KEY` for production
- Set `DEBUG=False` in production
- Use environment variables for sensitive data
- Enable HTTPS (automatic on Railway/Render)

---

## 📞 Domain Setup (General)

Once you deploy, you'll get a URL like:
- Railway: `your-app.railway.app`
- Render: `your-app.onrender.com`
- Fly.io: `your-app.fly.dev`

To connect your custom domain:
1. Go to your hosting platform's domain settings
2. Add your domain (e.g., `tiktokshopradar.com`)
3. Copy the CNAME/A records provided
4. Add them to your domain registrar's DNS settings
5. Wait for DNS propagation (5-30 minutes)

**Typical DNS Records:**
```
Type: CNAME
Name: @ or www
Value: [provided by hosting platform]
```

---

Ready to deploy! Let me know which platform you choose and I can provide more specific guidance.
