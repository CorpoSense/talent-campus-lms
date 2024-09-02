/* eslint-disable react/prop-types */
import { useState } from "react";
export const SearchBar=(props)=>
{
    let [val,setValue]=useState("") ;
    function handleChange(e)
    {
     setValue(e.target.value);
    }
    function HandleSearch(e)
    {
    e.preventDefault();
    console.log(val)
    }
    return (
        <>
    <form action="/search" className=" ">
        <div className="relative ">
            <input value={val} onChange={(e)=>{handleChange(e)}} type="text" name="q" className={props.apply ? 'lg:w-[500px] md:w-[250px] pl-10 xs:w-[200px] w-[140px] outline-none p-4 rounded-[3px] md:h-[45px] h-[38px] placeholder:text-black md:placeholder:text-[14px] placeholder:text-[12px] font-medium sm:text-[14px] text-[12px] border border-black text-black bg-white' : 'lg:w-[500px] md:w-[250px] pl-10 xs:w-[200px] w-[140px] shadow outline-none p-4 rounded-[3px] md:h-[45px] h-[38px] placeholder:text-[#8a9ca7] md:placeholder:text-[14px] placeholder:text-[12px] font-medium sm:text-[14px] text-[12px] text-[#8a9ca7] bg-[#f2f2f2]'} placeholder="Search"/>
            <button onClick={HandleSearch} type="submit">
                <svg className={props.apply ? 'text-black md:h-4 md:w-4 x-3 h-3 top-[15px] absolute md:top-[15px]  left-2 fill-current ' :'text-[#A7B5BE] md:h-4 md:w-4 x-3 h-3 top-[15px] absolute md:top-[15px]  left-2 fill-current '} 
                    xmlns="http://www.w3.org/2000/svg" version="1.1"
                    x="0px" y="0px" viewBox="0 0 56.966 56.966"
                  >
                    <path
                        d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z">
                    </path>
                </svg>
            </button>
        </div>
    </form>
        </>
    )
}