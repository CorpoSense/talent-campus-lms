# TalentCampus - LMS

<div align="center">
  <a href="https://gitpod.io/from-referrer/">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Logo" width="auto">
  </a>

  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
</div>

TalentCampus is an innovative Learning Management System (LMS) designed to bridge the gap between education and employment. Our platform provides a seamless, interactive, and comprehensive learning experience for students, educators, and employers.

## Project Vision

We envision a world where students are not only academically proficient but also well-prepared for the dynamic demands of the job market. TalentCampus aims to cultivate a community of lifelong learners, innovators, and leaders by providing access to quality education, practical experience, and career opportunities.

## Key Features

- Personalized Learning Paths
- Interactive Courses and Materials
- Mentorship and Networking
- Career Opportunities
- Integrated Assessments
- Certification and Recognition
- Community Engagement
- Exclusive Offers and Discounts

## Build & Testing

```bash
# Build the UI
echo "Building UI"
cd ui/
pnpm i
cp .env.example .env
pnpm test
pnpm build
cd ..

# Build the backend API
echo "Building backend API ..."
pip install -r requirements.txt
cp .env.example .env
# Generate a SECRET_KEY in .env file if necessary

# Generate static assets
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py test

# Run dev server (DEBUG mode)
echo "To run in DEBUG mode:"
echo "DEBUG=True python manage.py runserver"

# Run prod server (ASGI)
echo "To run in production mode:"
echo "DEBUG=False uvicorn backend_lms.asgi:application --host 0.0.0.0 --port 8000 --workers 2"
```

P.S. You may need to adjust `host`, `port`, `workers` (4, 8...) according to your requirements.