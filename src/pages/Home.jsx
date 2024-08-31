/* eslint-disable no-unused-vars */
import { data } from "../data/data"
import { Hero } from "../components/Hero"
import students from "/students.svg";
import camera from "/camera.svg";
import users from "/users.svg";
import graduation from "/graduation.svg";
import { Item } from "../components/Item";
import { Slide } from "../components/Slider";
import { Category } from "../components/Category";
import { categories } from "../data/data";
import { Feedback } from "../components/Feedback";
import { FeedbackSlider } from "../components/FeedbackSlider";
import { Link } from "react-router-dom";
import { Footer } from "../components/Footer";
export const Home=()=>
{
    
    const settings = {
        dots: true,
        
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3
      };
return (
    <div className="min-h-[100vh]  mx-auto w-[90%]">
    <Hero/> 
          <div className="flex mb-10 space-y-10 flex-col items-center">
            <h1 className="text-4xl text-center tracking-wide	  font-bold">
                What is 
                <span className=" bg-gradient-to-r from-[rgb(121,165,212)] to-[rgb(32,180,134)]    inline-block  text-transparent bg-clip-text ">
                 Talent campus  ?              </span>
            </h1>
          
            <p className="text-center text-[17px] w-[70%] leading-7 sm:text-left">
            Talent Campus is a versatile platform that enables educators to create and manage online courses with ease. Instructors can store materials, handle assignments, quizzes, and exams, monitor deadlines, grade work, and provide feedback—all in one streamlined place.
            </p>
            <div  className="bg-[#e7f2ff]  w-[100vw] flex justify-between h-[80px]">
                <div className="flex w-[90vw] flex-row justify-between  mx-auto">
                <Item src={graduation} nb={300} name="Constructor" />
                <Item src={students} nb={"20,000"} name="Student" />
                <Item src={camera} nb={"10,000"} name="Video" />  
                <Item src={users} nb={"100,000"} name="Users" />

                 </div>
            
            </div>
            <h1 className="text-4xl w-[90vw] text-center tracking-wid   font-bold">
                Most   <span className="bg-gradient-to-r from-[#007bff] to-[rgb(32,180,134)]  inline-block text-transparent bg-clip-text"> 
                Popular Courses
            </span>
            </h1>     
             
        </div>
       
       <Slide/>
       <div className="flex flex-col mt-10 items-center ">
       <div className="  space-y-10 items-center mt-10 py-20 h-fit mb-10 bg-[#e7f2ff] w-[100vw]  ">
        
       <h1 className="text-4xl tracking-wide text-center mt-10 font-bold">
                Most   <span className="bg-gradient-to-r from-[#007bff] to-[rgb(32,180,134)]  inline-block text-transparent bg-clip-text"> 
                Popular Catgories
            </span>
            </h1> 
            <div className="mx-auto  grid grid-cols-4 gap-4  w-[90vw]">
           
     {
categories.map((item)=>
{
    return (
        <Category key={item.id} img={item.img} name={item.name} />
    )
})
     }
            </div>
         </div>
       
       </div>

        <h1 className="text-4xl text-center tracking-wide  my-10 font-bold">
                Students   <span className="bg-gradient-to-r from-[#007bff] to-[rgb(32,180,134)]  inline-block text-transparent bg-clip-text"> 
                Feedback
            </span>
            </h1> 
            <FeedbackSlider/>
            <h1 className="text-4xl  text-center tracking-wide  my-10 font-bold">
                Join   <span className="bg-gradient-to-r from-[#007bff] to-[rgb(32,180,134)] mt-10  inline-block text-transparent bg-clip-text mr-2"> 
                the world's largest
            </span>
             learning platform today !
            </h1> 
            <h1 className="text-center font-semibold text-[#52565C]">
            Start learning by registering for free
            </h1>
            <div className="flex flex-col justify-center">
            <p className="text-center text-[#52565C] ">
            Ut pharetra ipsum nec leo blandit, sit amet tincidunt eros pharetra. Nam sed imperdiet turpis. In hac habitasse platea dictumst. <br></br>
            Praesent nulla massa, hendrerit vestibulum gravida in, feugiat auctor felis.
            </p>
            <button className="w-[200px] bg-[#20b486]  justify-center  text-white rounded-[2px] px-[10px] py-[10px] sm:py-[12px]  items-center mx-auto my-10">
                <Link to="/Signup">
                Register for free 

</Link></button>
            </div>
          <Footer/>
    </div>
)
}