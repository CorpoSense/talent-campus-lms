import computer from "../../public/computer.svg";
import { useFormik } from "formik";
import { Link} from "react-router-dom";
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";

export const Signup = () => {
  const handleForget = () => {
    // Handle forgot password logic
  };

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
      firstName :"" ,
      name:"" ,
    },
    validationSchema: basicschema,
    onSubmit: (values) => {
      console.log('here are th values'+ values);
      // Handle form submission logic
    },
  });
  const handleSubmit=()=>
  {
    console.log(formik.values);
  }

  return (
   
        <div className=" ">
        <div className="flex sm:flex-row flex-col-reverse py-5 w-[90%] justify-center items-center sm:justify-between  mx-auto ">
        <form
          onSubmit={formik.handleSubmit}
          className="flex flex-col space-y-2"
        >
          
          <h1 className="font-bold text-xl xxs:text-3xl bg-gradient-to-r from-[#20b486]  to-[#007bff] inline-block text-transparent bg-clip-text ">Create an account</h1>
          <Input
              id="firstName"
              name="firstName"  // Add the name attribute  here
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
              name="name"  // Add the name attribute  here
              label="Last name"
              value={formik.values.name}
              onChange={formik.handleChange}
              placeholder="Enter your last name"
            />
              {formik.errors.name && formik.touched.name && (
            <div className="text-red-500 text-[12px]">{formik.errors.name}</div>
          )}
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
          <Input
            id="password"
            type="password"
            label="Password"
            name="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            placeholder="Enter your password"
          />
          {formik.errors.password && formik.touched.password && (
            <div className="text-red-500 text-[12px]">{formik.errors.password}</div>
          )}
          <h1
            onClick={handleForget}
            className="text-right underline cursor-pointer text-[12px] md:text-[14px] text-[#202121]/80"
          >
            <Link to="./ForgetPassword">Forget password?</Link>
          </h1>
          <div className="flex justify-around">
            <input type="checkbox">
            </input>
           <p className="text-[10px]">
            By creating an account, I agree to our Terms of use  and Privacy Policy 
           </p>
          </div>
          <button onClick={handleSubmit}
            type="submit"
            className="bg-[#20b486] text-white  rounded-[2px] px-[10px] py-[8px] "
          >
          Create an account 
          </button>
          <h1 className="text-right underline cursor-pointer text-[12px] md:text-[14px] text-[#202121]/80">
            <Link to="./Login">Login in instead</Link>
          </h1>
        </form>
        <img
          src={computer}
          className="lg:w-[400px] font-['Lato']  md:w-[350px] xxs:w-[250px] w-[200px]"
        />
      </div>
        </div>
     

  );
};
