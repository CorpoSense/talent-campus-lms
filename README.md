# TalentCampus - LMS

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

## Build

```bash
# Build the UI
cd ui
pnpm build
cd ..

# Generate static assets
python manage.py collectstatic

# run dev server
python manage.py collectstatic

# run prod server (WSGI)
gunicorn backend_lms.wsgi:application --bind 0.0.0.0:8000 --workers 2

# run prod server (ASGI)
uvicorn backend_lms.asgi:application --host 0.0.0.0 --port 8000 --workers 2
```
P.S. You may need to ajust `host`, `port`, `workers` (4, 8...) according to your requirements.