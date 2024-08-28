import computer from "../../public/computer.svg";
import { useFormik } from "formik";
import { Link, BrowserRouter as Router } from "react-router-dom";
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";

export const Login = () => {
  const handleForget = () => {
    // Handle forgot password logic
  };

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: basicschema,
    onSubmit: (values) => {
      console.log("Form Submitted with values:", values); // Logging form values
    },
  });
  const handleLogin = () => {
    console.log(formik.values)
  }

  return (
    
      <div className="flex sm:flex-row flex-col-reverse py-5 w-[90%] justify-center items-center sm:justify-between min-h-[100vh] mx-auto sm:h-[80vh]">
        <form
          onSubmit={formik.handleSubmit}
          className="flex flex-col space-y-2"
        >
          <h1 className="text-[#007bff] font-bold text-3xl">Log In</h1>
          <Input
            id="email"
            name="email" // Ensure 'name' is present and matches 'initialValues'
            type="email"
            label="Email"
            value={formik.values.email}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur} // Trigger validation on blur
            placeholder="Enter your email"
          />
          {formik.errors.email && formik.touched.email && (
            <div className="text-red-500 text-sm">{formik.errors.email}</div>
          )}
          <Input
            id="password"
            name="password" // Ensure 'name' is present and matches 'initialValues'
            type="password"
            label="Password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur} // Trigger validation on blur
            placeholder="Enter your password"
          />
          {formik.errors.password && formik.touched.password && (
            <div className="text-red-500 text-sm">{formik.errors.password}</div>
          )}
          <h1
            onClick={handleForget}
            className="text-right underline cursor-pointer text-[12px] md:text-[15px] text-[#202121]/80"
          >
            <Link to="./ForgetPassword">Forget password?</Link>
          </h1>
          <button onClick={handleLogin}
            type="submit"
            className="bg-[#20b486] text-white rounded-[2px] px-[10px] py-[8px]"
          >
            Log In
          </button>
          <h1 className="text-right underline cursor-pointer text-[12px] md:text-[15px] text-[#202121]/80">
            <Link to="./Signup">Sign Up instead</Link>
          </h1>
        </form>
        <img
          src={computer}
          className="lg:w-[400px] font-['Lato'] md:w-[350px] xxs:w-[250px] w-[200px]"
        />
      </div>

  );
};
