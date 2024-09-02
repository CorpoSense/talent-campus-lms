/* eslint-disable no-unused-vars */
import { useState } from "react"
import { Navbar } from "../components/Navbar"
import { Slide } from "../components/Slider";
import { SlideConnected } from "../components/SliderConnected";
import { Pagination } from "../components/pagination";
import { ChevronDownIcon } from '@heroicons/react/24/solid';
import { Link } from 'react-router-dom';
import { Footer } from "../components/Footer";
import { Search } from "../components/Search";
export const Courses=()=>
    {
        
        return (
            <>
                            <Navbar/>

             <div className="w-[90vw] flex flex-col space-y-20 mx-auto">
<div className="flex flex-row items-end  justify-between">
<h1 className="md:text-4xl text-xl sm:text-2xl tracking-wide text-left mt-10 font-bold">
                 <span className="bg-gradient-to-r from-[rgb(0,123,255)] to-[rgb(32,180,134)]  inline-block text-transparent bg-clip-text"> 
                 Welcome back, ready for your next lesson?
            </span></h1> 
<h1 className="text-[rgb(32,180,134)] sm:text-[17px] text-[12px] font-bold hover:underline cursor-pointer">
                See all </h1>
</div>
            </div>
            <SlideConnected/>    
<h1 className="mt-20 mb-5 w-[90vw] mx-auto font-bold text-xl text-[rgb(0,123,255)] md:text-3xl sm:text-2xl text-left">
    Choose course
</h1>

  
      <Search/>   
            </>
           
        )
    } 