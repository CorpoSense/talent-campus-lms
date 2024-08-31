import { Link } from "react-router-dom"
export const Footer=()=>
{
    return (
        <div className="my-10 flex flex-col">
             <div className="w-[90%] mx-auto justify-between items-start flex flex-row  ">
     <div className="flex space-y-4 sm:w-[30%] w-[45%] flex-col">
        <h1 className="font-bold">
            Contact Us
        </h1>
        <h1 className="text-[#343a40] text-[12px]">
        Call : +123 400 123
        </h1> 
        <h1 className="text-[#343a40] text-[12px]">
          Praesent nulla massa, hendrerit vestibulum gravida in, feugiat auctor felis.       
        </h1>    <h1 className="text-[#343a40] text-[12px]">
        Email: example@mail.com        </h1>        
     </div>
     <div className="sm:w-[30%] flex flex-col items-center space-y-4 w-[45%]">
     <h1 className="font-bold">
Explore        </h1>
<h1 className="text-[#343a40] text-[12px]">
    <Link to='/'>
    Home
    </Link>
       
 </h1> <h1 className="text-[#343a40] text-[12px]">
Courses       
 </h1> <h1 className="text-[#343a40] text-[12px]">
Contact       
 </h1> 
     </div>
     <div>


     </div>
     <h3 className=' text-3xl sm:block hidden'> <span className='text-[#ffc107] font-bold italic'>Talent</span>  <span className='text-[#20b486] italic font-bold'>Campus
          </span> </h3>
            </div>
             <h1 className="text-[#343a40] text-[12px]">
Contact       
 </h1>     
        </div>
    )
}