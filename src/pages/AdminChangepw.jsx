import  { useState } from 'react';
import { AdminNavbar } from '../components/AdminNavbar';
import { useFormik } from "formik";
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";
import { FaEye, FaEyeSlash } from 'react-icons/fa'; // Importing the icons
import profile from '../../public/profile.svg';
import logout from '../../public/logout.svg';

export const AdminChangepw = () => {
  const [activeLink, setActiveLink] = useState('Changepassword');
  const [showCurrentPw, setShowCurrentPw] = useState(false);
  const [showNewPw, setShowNewPw] = useState(false);
  const [showConfirmPw, setShowConfirmPw] = useState(false);

  const formik = useFormik({
    initialValues: {
      email: "",
      current_pw: "",
      new_pw: "",
      confirm_pw: "",
    },
    validationSchema: basicschema,
    onSubmit: (values) => {
      console.log("Form Submitted with values:", values);
    },
  });

  const handleEdit = () => {
    console.log(formik.values);
  };

  return (
    <>
      <AdminNavbar />
      <div className="min-h-[90vh] mx-auto w-[90%] flex flex-col lg:flex-row mt-9 lg:space-x-6 mb-10">
        {/* Profile Header */}
        <div className="bg-white shadow-md rounded-lg p-9 w-full lg:w-[30%] flex flex-col items-center space-y-10 mb-10 lg:mb-0">
          <div>
            <img
              src={profile}
              className="lg:w-[80px] font-['Lato'] md:w-[350px] xxs:w-[250px] w-[200px] mr-12"
              alt="Profile"
            />
            <h1 className="font-bold">User's full name</h1>
            <h4>useremail@gmail.com</h4>
          </div>
          <hr className="my-4 border-t-2 border-gray-300" />
          {/* Navigation Links */}
          <div>
            <ul className="text-[#6D737A] text-[15px] b-sm:justify-around mb-10 gap-10 space-y-4">
              <li>
                <a
                  href="#Editprofil"
                  onClick={() => setActiveLink('Editprofil')}
                  className={activeLink === 'Editprofil' ? 'text-[#20B486] font-bold' : ''}
                >
                  Edit Profil
                </a>
              </li>
              <li>
                <a
                  href="#Changepassword"
                  onClick={() => setActiveLink('Changepassword')}
                  className={activeLink === 'Changepassword' ? 'text-[#20B486] font-bold' : ''}
                >
                  Change Password
                </a>
              </li>
            </ul>
          </div>
          {/* Logout */}
          <div className="relative">
            <a href="#logout" className="flex items-center text-red-500 font-bold">
              <img src={logout} alt="Logout Icon" className="w-4 h-4 -ml-10" />
              <span>Log out</span>
            </a>
          </div>
        </div>

        {/* Change Password Form */}
        <div className="bg-white shadow-md rounded-lg p-6 w-full lg:w-[70%] flex flex-col items-center lg:flex-row lg:items-start lg:space-x-20">
          <form onSubmit={formik.handleSubmit} className="flex flex-col space-y-4 ml-10">
            <h1 className="text-[#007bff] font-bold text-3xl text-gradient mt-3">Change Password</h1>
            <Input
              id="email"
              type="email"
              label="Email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
              placeholder="Enter your email"
            />
            {formik.errors.email && formik.touched.email && (
              <div className="text-red-500 text-[12px]">{formik.errors.email}</div>
            )}

            <div className="relative">
              <Input
                id="current_pw"
                name="current_pw"
                label="Current Password"
                type={showCurrentPw ? "text" : "password"}
                value={formik.values.current_pw}
                onChange={formik.handleChange}
                placeholder="Enter your current password"
              />
              <div className="absolute inset-y-10 right-0 pr-3 flex items-center">
                {showCurrentPw ? (
                  <FaEyeSlash onClick={() => setShowCurrentPw(!showCurrentPw)} />
                ) : (
                  <FaEye onClick={() => setShowCurrentPw(!showCurrentPw)} />
                )}
              </div>
            </div>
            {formik.errors.current_pw && formik.touched.current_pw && (
              <div className="text-red-500 text-[12px]">{formik.errors.current_pw}</div>
            )}

            <div className="relative">
              <Input
                id="new_pw"
                name="new_pw"
                label="New Password"
                type={showNewPw ? "text" : "password"}
                value={formik.values.new_pw}
                onChange={formik.handleChange}
                placeholder="Enter your new password"
              />
              <div className="absolute inset-y-10 right-0 pr-3 flex items-center">
                {showNewPw ? (
                  <FaEyeSlash onClick={() => setShowNewPw(!showNewPw)} />
                ) : (
                  <FaEye onClick={() => setShowNewPw(!showNewPw)} />
                )}
              </div>
            </div>
            {formik.errors.new_pw && formik.touched.new_pw && (
              <div className="text-red-500 text-[12px]">{formik.errors.new_pw}</div>
            )}

            <div className="relative">
              <Input
                id="confirm_pw"
                name="confirm_pw"
                label="Confirm Password"
                type={showConfirmPw ? "text" : "password"}
                value={formik.values.confirm_pw}
                onChange={formik.handleChange}
                placeholder="Enter your new password"
              />
              <div className="absolute inset-y-10 right-0 pr-3 flex items-center">
                {showConfirmPw ? (
                  <FaEyeSlash onClick={() => setShowConfirmPw(!showConfirmPw)} />
                ) : (
                  <FaEye onClick={() => setShowConfirmPw(!showConfirmPw)} />
                )}
              </div>
            </div>
            {formik.errors.confirm_pw && formik.touched.confirm_pw && (
              <div className="text-red-500 text-[12px]">{formik.errors.confirm_pw}</div>
            )}

            <button
              onClick={handleEdit}
              type="submit"
              className="bg-[#20b486] text-white rounded-[2px] px-[10px] py-[8px]"
            >
              Change
            </button>
          </form>
          <img
            src={profile}
            className="lg:w-[150px] font-['Lato'] md:w-[20px] xxs:w-[150px] w-[150px] items-center mt-24 transform -translate-x-5"
            alt="Profile"
          />
        </div>
      </div>
    </>
  );
};
