/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import { Feedbacks } from "../data/data";
import guillemets from "/guillemets.svg";

export const Feedback=(props)=>
{
 return (
    <div className=" min-h-[200px] shadow rounded-[8px] w-[92%] bg-white space-y-4 px-6 p-3 items-left flex flex-col">
        <div className="flex justify-between flex-row items-start"> 
                   
<div className="flex space-x-2 flex-row items-center">
<img className="w-[50px] md:w-[70px]" src={props.img} />
            <div className="flex flex-col">
            <h1 className="font-bold text-left text-[13px] md:text-lg">
  {  props.name }   </h1>
  <h1 className="sm:text-[12px] text-[10px]">
  { props.profession } 
    </h1> 
            </div>
</div>
           
            <img className="md:w-[20px] w-[12px]  " src={guillemets}/> 

        </div>
       <p className="sm:text-[14px] text-[11px]">
    {  props.details }   
 
       </p>
       

    </div>
 )
}