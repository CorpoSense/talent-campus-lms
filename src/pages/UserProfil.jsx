import React, { useState } from 'react';
import { Navbar } from '../components/Navbar';
import { useFormik } from "formik";
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";
import profile from '../../public/profile.svg';
import logout from '../../public/logout.svg'; 

export const    UserProfil = () => {
  const [activeLink, setActiveLink] = useState('Editprofil'); // Track active link

  const formik = useFormik({
    initialValues: {
      Firstname: "",
      Lastname: "",
    },
    validationSchema: basicschema,
    onSubmit: (values) => {
      console.log("Form Submitted with values:", values); // Editing form values
    },
  });

  const handleEdit = () => {
    console.log(formik.values);
  };

  return (
    <>
      <Navbar />
      <div className="min-h-[90vh] mx-auto w-[90%] flex flex-col lg:flex-row mt-9 lg:space-x-6 mb-10"> {/* Adding space between the two divs */}
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
      href="/profil"
      onClick={() => setActiveLink('Editprofil')}
      className={activeLink === 'Editprofil' ? 'text-[#20B486] font-bold' : ''}
    >
      Edit Profil
    </a>
  </li>
              <li>
    <a
      href="/changepassword"
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

        {/* Edit Profile Form */}
        <div className="bg-white shadow-md rounded-lg p-6 w-full lg:w-[70%] flex flex-col items-center lg:flex-row lg:items-start lg:space-x-10  ">
        <form onSubmit={formik.handleSubmit} className="flex flex-col space-y-4">            <h1 className="text-[#007bff] font-bold text-3xl text-gradient mt-20">Edit Profil</h1>
            <Input
              id="firstName"
              name="firstName"
              label="First name"
              value={formik.values.firstName}
              onChange={formik.handleChange}
              placeholder="Enter your first name"
            />
            {formik.errors.firstName && formik.touched.firstName && (
              <div className="text-red-500 text-[12px]">{formik.errors.firstName}</div>
            )}

            <Input
              id="name"
              name="name"
              label="Last name"
              value={formik.values.name}
              onChange={formik.handleChange}
              placeholder="Enter your last name"
            />
            {formik.errors.name && formik.touched.name && (
              <div className="text-red-500 text-[12px]">{formik.errors.name}</div>
            )}

       <button
            onClick={handleEdit}
            type="submit"
            className="bg-[#20b486] text-white rounded-[2px] px-[10px] py-[8px]"
          >
            Save
          </button>
          </form>
          <img
  src={profile}
  className="lg:w-[150px] font-['Lato'] md:w-[20px] xxs:w-[150px] w-[150px] items-center mt-24 transform translate-x-20"
  alt="Profile"
/>

        </div>
      </div>
    </>
  );
};
