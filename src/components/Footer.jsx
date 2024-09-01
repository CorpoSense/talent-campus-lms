import { Link } from "react-router-dom";

export const Footer = () => {
  return (
    <div className="mt-20 mx-auto flex flex-col">
      <div className="w-[100%] mx-auto justify-between items-start flex flex-row">
        <div className="flex space-y-4 sm:w-[30%] w-[45%] flex-col z-20">
          <h1 className="font-bold">Contact Us</h1>
          <h1 className="text-[#343a40] text-[14px]">Call : +123 400 123</h1>
          <h1 className="text-[#343a40] text-[14px]">
            Praesent nulla massa, hendrerit vestibulum gravida in, feugiat auctor felis.
          </h1>
          <h1 className="text-[#343a40] text-[14px]">Email: example@mail.com</h1>
        </div>
        <div className="sm:w-[30%] flex flex-col items-center space-y-4 w-[45%] z-20">
          <h1 className="font-bold">Explore</h1>
          <h1 className="text-[#343a40] text-[14px]">
            <Link to="/">Home</Link>
          </h1>
          <h1 className="text-[#343a40] text-[14px]">
            <Link to="/Courses">Courses</Link>
          </h1>
          <h1 className="text-[#343a40] text-[14px]">
            <Link to="/Contact">Contact</Link>
          </h1>
        </div>
        <div></div>
        <h3 className="text-3xl sm:block hidden z-20">
          <span className="text-[#ffc107] font-bold italic">Talent</span>{" "}
          <span className="text-[#20b486] italic font-bold">Campus</span>
        </h3>
      </div>
      <div className="flex flex-row items-end justify-between z-20">
        <div className="flex flex-row justify-between mt-20 text-[#343a40] text-[14px] space-x-2 mx-auto">
          <span>
            <Link to="Careers">Careers</Link>
          </span>
          <span>|</span>
          <span>
            <Link to="PrivacyPolicy">Privacy Policy</Link>
          </span>
          <span>|</span>
          <span>
            <Link to="/terms&conditions">Terms & conditions</Link>
          </span>
        </div>
      </div>
      <p className="text-center mb-10 text-[#343a40] text-[14px] mt-20 z-20">
        © 2024 Class Technologies Inc.
      </p>
   
    </div>
  );
};
