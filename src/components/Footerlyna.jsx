import React from 'react';
import fb from '../../public/fb.svg';
import Dribbble from '../../public/Dribbble.svg';
import linkedin from '../../public/linkedin.svg';
import insta from '../../public/insta.svg';
import Behance from '../../public/Behance.svg';

// If using React Router for navigation
import { Link } from 'react-router-dom';

export const Footer = () => {
  return (
    <footer className="bg-gradient-to-r from-[#A8DFF5] via-[#F8D7C4] via-[#F2F1E0] to-white py-8 font-['Lato']">
      <div className="container mx-auto flex flex-col md:flex-row justify-center items-center space-x-60 mb-20">
        {/* Social Media Links */}
        <div className='space-x-20 flex justify-center'>
          <div className='space-y-4 mt-20'>
            <ul className="flex flex-col space-y-4 text-[#343A40]">
              <li className="font-bold text-[#202121] text-[24px]">Contact Us</li>
              <li className="text-[16px]">Call: +123 400 123</li>
              <li className="text-[16px]">
                Praesent nulla massa, hendrerit vestibulum
                <br />
                gravida in, feugiat auctor felis.
              </li>
              <li className="text-[16px]">Email: example@mail.com</li>
            </ul>

            <div className="flex space-x-4 text-[#343A40]">
              <button className="w-[40px] h-[40px] rounded-full bg-white flex items-center justify-center">
                <a href="https://www.facebook.com">
                  <img src={fb} className='w-[18px] h-[18px]' alt="facebook" />
                </a>
              </button>

              <button className="w-[40px] h-[40px] rounded-full bg-white flex items-center justify-center">
                <a href="https://www.dribbble.com">
                  <img src={Dribbble} className='w-[18px] h-[18px]' alt="Dribbble" />
                </a>
              </button>

              <button className="w-[40px] h-[40px] rounded-full bg-white flex items-center justify-center">
                <a href="https://www.linkedin.com">
                  <img src={linkedin} className='w-[18px] h-[18px]' alt="linkedin" />
                </a>
              </button>

              <button className="w-[40px] h-[40px] rounded-full bg-white flex items-center justify-center">
                <a href="https://www.instagram.com">
                  <img src={insta} className='w-[18px] h-[18px]' alt="insta" />
                </a>
              </button>

              <button className="w-[40px] h-[40px] rounded-full bg-white flex items-center justify-center">
                <a href="https://www.behance.net/">
                  <img src={Behance} className='w-[18px] h-[18px]' alt="Behance" />
                </a>
              </button>
            </div>
          </div>

          <div className="flex items-center">
            {/* Navigation Links */}
            <ul className="flex flex-col items-center space-y-4 text-[#343A40]">
              <li className="font-bold text-[#202121] text-[24px]">Explore</li>
              <li className="text-[16px]">
                <a href="#about" className="hover:text-[#ffc107]">Home</a>
              </li>
              <li className="text-[16px]">
                <a href="#courses" className="hover:text-[#ffc107]">Courses</a>
              </li>
              <li className="text-[16px]">
                <a href="#contact" className="hover:text-[#ffc107]">Contact</a>
              </li>
            </ul>
          </div>
        </div>

        {/* Logo and Company Name */}
        <div className="mb-4 md:mb-0 mt-10">
          <h3 className="text-[45px] font-pt-serif">
            <span className='text-[#ffc107] font-bold italic'>Talent</span>
            <span className='text-[#20b486] italic font-bold mr-6'>Campus</span>
          </h3>
        </div>
      </div>

      {/* Links to Pages */}
      <div>
        <ul className="flex justify-center items-center text-[#343A40]">
          <li className="text-[16px] relative">
            <Link to="/careers" className="hover:text-[#ffc107]">Careers</Link>
          </li>
          <li className="text-[16px] relative before:content-['|'] before:px-2 before:text-[#343A40]">
            <Link to="/privacypolicy" className="hover:text-[#ffc107]">Privacy Policy</Link>
          </li>
          <li className="text-[16px] relative before:content-['|'] before:px-2 before:text-[#343A40]">
            <Link to="/termsandconditions" className="hover:text-[#ffc107]">Terms & Conditions</Link>
          </li>
        </ul>
      </div>

      {/* Copyright */}
      <div className="mt-8 text-center text-[#343A40]">
        <p>&copy; 2021 Class Technologies Inc.</p>
      </div>
    </footer>
  );
};
