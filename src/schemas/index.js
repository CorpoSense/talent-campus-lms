/* eslint-disable no-unused-vars */
import * as yup from 'yup';
export const basicschema=yup.object().shape({
    email : yup.string().email("please enter a valid email !").required("This field is required !"),
   password : yup.string().required("This field is required").min(8,"password must be atleast 8 characters !") ,
   confirmpassword : yup.string().oneOf([yup.ref("password"),null],"Passwords must match").required("This field is required"),
   name : yup.string().required("This field is required !"),
   firstName : yup.string().required("This field is required !"),
   JobTitle: yup.string().required("This field is required !"),
      CompanyName:yup.string().required("This field is required !"),
      Location :yup.string().required("This field is required !") ,
      Experience:yup.string().required("This field is required !"),
      ContactType:yup.string().required("This field is required !"),
      JobDescreption:yup.string().required("This field is required !"),
      Responsibilities:yup.string().required("This field is required !"),
      Skills:yup.string().required("This field is required !"),
      Benefits:yup.string().required("This field is required !"),
      ApplyMethod:yup.string().required("This field is required !"),
})