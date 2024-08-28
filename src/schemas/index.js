/* eslint-disable no-unused-vars */
import * as yup from 'yup';
export const basicschema=yup.object().shape({
    email : yup.string().email("please enter a valid email !").required("This field is required !"),
   password : yup.string().required("This field is required").min(8,"password must be atleast 8 characters !") ,
   confirmpassword : yup.string().oneOf([yup.ref("password"),null],"Passwords must match").required("This field is required"),
   name : yup.string().required("This field is required !"),
   firstName : yup.string().required("This field is required !"),
})