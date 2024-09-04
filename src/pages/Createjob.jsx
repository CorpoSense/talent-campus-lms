import { useFormik } from "formik";
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";
import { AdminNavbar } from "../components/AdminNavbar";
import { useState } from "react";
import { Footer } from "../components/Footerlyna";

export const Createjob = () => {
  const [isFullTime, setIsFullTime] = useState(false);
  const [isPartTime, setIsPartTime] = useState(false);

  const formik = useFormik({
    initialValues: {
      JobTitle: "",
      CompanyName: "",
      Location: "",
      Experience: "",
      ContactType: "",
      JobDescreption: "",
      Responsibilities: "",
      Skills: "",
      Benefits: "",
      ApplyMethod: ""
    },
    validationSchema: basicschema,
    onSubmit: (values) => {
      console.log('Here are the values: ', { ...values, isFullTime, isPartTime });
      // Handle form submission logic
    },
  });

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    if (name === "isFullTime") {
      setIsFullTime(checked);
    } else if (name === "isPartTime") {
      setIsPartTime(checked);
    }
  };

  const handleSubmit = () => {
    console.log({ ...formik.values, isFullTime, isPartTime });
  };

  return (
    <>
      <AdminNavbar />
      <div className=" ">
        <div className="flex sm:flex-row flex-col-reverse py-5 justify-center items-center sm:justify-between mx-auto  ">
          <form
            onSubmit={formik.handleSubmit}
            className="flex flex-col space-y-2 ml-8"
          >
            <h1 className="font-bold text-xl xxs:text-3xl bg-gradient-to-r from-[#20b486]  to-[#007bff] inline-block text-transparent bg-clip-text ">
              Create a Job
            </h1>

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="JobTitle"
            >
              Job Title :
            </label>
            <Input
              id="JobTitle"
              name="JobTitle"
              value={formik.values.JobTitle}
              onChange={formik.handleChange}
              className="w-full"
            />
            {formik.errors.JobTitle && formik.touched.JobTitle && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.JobTitle}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="CompanyName"
            >
              Company Name :
            </label>
            <Input
              id="CompanyName"
              name="CompanyName"
              value={formik.values.CompanyName}
              onChange={formik.handleChange}
            />
            {formik.errors.CompanyName && formik.touched.CompanyName && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.CompanyName}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="Location"
            >
              Location :
            </label>
            <Input
              id="Location"
              name="Location"
              value={formik.values.Location}
              onChange={formik.handleChange}
            />
            {formik.errors.Location && formik.touched.Location && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.Location}
              </div>
            )}

            {/* Job Type Label and Checkboxes */}
            <label className="text-[#202121]/80 text-left text-[14px]">
              Job Type:
            </label>
            <div className="flex flex-col space-y-2">
              <label className="flex items-center text-[#202121]/80 text-[14px]">
                <input
                  type="checkbox"
                  name="isFullTime"
                  checked={isFullTime}
                  onChange={handleCheckboxChange}
                  className="mr-2"
                />
                Full-Time
              </label>
              <label className="flex items-center text-[#202121]/80 text-[14px]">
                <input
                  type="checkbox"
                  name="isPartTime"
                  checked={isPartTime}
                  onChange={handleCheckboxChange}
                  className="mr-2"
                />
                Part-Time
              </label>
            </div>

            {/* Rest of your form fields */}
            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="Experience"
            >
              Experience :
            </label>
            <Input
              id="Experience"
              name="Experience"
              value={formik.values.Experience}
              onChange={formik.handleChange}
            />
            {formik.errors.Experience && formik.touched.Experience && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.Experience}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="ContactType"
            >
              Contact Type :
            </label>
            <Input
              id="ContactType"
              name="ContactType"
              value={formik.values.ContactType}
              onChange={formik.handleChange}
            />
            {formik.errors.ContactType && formik.touched.ContactType && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.ContactType}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="JobDescreption"
            >
              Job Descreption :
            </label>
            <Input
              id="JobDescreption"
              name="JobDescreption"
              value={formik.values.JobDescreption}
              onChange={formik.handleChange}
            />
            {formik.errors.JobDescreption && formik.touched.JobDescreption && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.JobDescreption}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="Responsibilities"
            >
              Responsibilities :
            </label>
            <Input
              id="Responsibilities"
              name="Responsibilities"
              value={formik.values.Responsibilities}
              onChange={formik.handleChange}
            />
            {formik.errors.Responsibilities && formik.touched.Responsibilities && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.Responsibilities}
              </div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="Skills"
            >
              Skills :
            </label>
            <Input
              id="Skills"
              name="Skills"
              value={formik.values.Skills}
              onChange={formik.handleChange}
            />
            {formik.errors.Skills && formik.touched.Skills && (
              <div className="text-red-500 text-[12px]">{formik.errors.Skills}</div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="Benefits"
            >
              Benefits :
            </label>
            <Input
              id="Benefits"
              name="Benefits"
              value={formik.values.Benefits}
              onChange={formik.handleChange}
            />
            {formik.errors.Benefits && formik.touched.Benefits && (
              <div className="text-red-500 text-[12px]">{formik.errors.Benefits}</div>
            )}

            <label
              className="text-[#202121]/80 text-left text-[14px]"
              htmlFor="ApplyMethod"
            >
              Apply Method :
            </label>
            <Input
              id="ApplyMethod"
              name="ApplyMethod"
              value={formik.values.ApplyMethod}
              onChange={formik.handleChange}
              className="w-full"
            />
            {formik.errors.ApplyMethod && formik.touched.ApplyMethod && (
              <div className="text-red-500 text-[12px]">
                {formik.errors.ApplyMethod}
              </div>
            )}
          </form>
        </div>
        <div>
          <button
            onClick={handleSubmit}
            type="submit"
            className="bg-[#20b486] text-white rounded-[2px] px-[40px] py-[8px] ml-80 mb-10"
          >
            Save
          </button>
        </div>
        <Footer />
      </div>
    </>
  );
};
