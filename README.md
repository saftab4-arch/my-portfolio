<<<<<<< HEAD
# Syed Aftab – Personal Portfolio

A personal portfolio website built with **Flask** and **HTML/CSS**, showcasing my IT experience, certifications, skills, and career goals.

## Tech Stack

- **Backend:** Python / Flask
- **Frontend:** HTML5, CSS3 (custom design, no frameworks)
- **Deployed on:** AWS EC2 (Amazon Linux 2023)
- **Color Palette:** Deep Teal, Forest Green, Light Lime, Sunny Yellow, Orange Red

## Features

- Hero section with links to LinkedIn and Credly badges
- Work experience timeline (IT Specialist, Help Desk, NOC, Healthcare IT)
- Education section (WGU Cybersecurity BS)
- 20+ certifications displayed in a card grid
- Skills grouped by category
- Contact section

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/saftab4-arch/my-portfolio.git
cd my-portfolio

# Install dependencies
pip3 install flask

# Run the app
python3 app.py
```

Then open your browser at `http://127.0.0.1:5000`

---

## Deploy on AWS EC2

### Step 1 – Launch EC2 Instance
- Go to AWS Console → EC2 → Launch Instance
- Choose **Amazon Linux 2023**
- Instance type: **t2.micro** (free tier)
- Create or select a key pair (.pem file)
- Launch the instance

### Step 2 – Open Port 5000 in Security Group
- Go to EC2 → Security Groups → select your group
- Click **Edit inbound rules** → **Add rule**
- Type: **Custom TCP** | Port: **5000** | Source: **0.0.0.0/0**
- Save rules

### Step 3 – SSH into your Instance
```bash
ssh -i your-key.pem ec2-user@YOUR_PUBLIC_IP
```

### Step 4 – Install Dependencies
```bash
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

### Step 5 – Clone the Repo
```bash
git clone https://github.com/saftab4-arch/my-portfolio.git
cd my-portfolio
```

### Step 6 – Install Flask
```bash
pip3 install flask
```

### Step 7 – Run the App
```bash
flask run --host=0.0.0.0 --port=5000
```

### Step 8 – Access the App
Open your browser and go to:
```
http://YOUR_PUBLIC_IP:5000
```

---

## Connect

- LinkedIn: [syed-b-9078141a8](https://www.linkedin.com/in/syed-b-9078141a8/)
- Credly: [syed-aftab](https://www.credly.com/users/syed-aftab.5fff51e0)
=======
Personal portfolio website built with Flask and HTML/CSS, showcasing my IT experience, 20+ certifications, and technical skills. Part of my AWS Bootcamp 2026 journey.
>>>>>>> 72ffe19d483fbcdcbdb910bf8d49992593447c93
