/* eslint-disable react/prop-types */
import arrow from "/arrow.svg";

export const Category=(props)=>
{
   return (
    <div className=" border-white border-[2px] hover:border-[yellow]  cursor-pointer flex  justify-between bg-white rounded-[10px] box-border min-h-[50px]  p-1">
<div className="flex items-center space-x-1 justify-between">
<img className="sm:w-[25px] w-[10px]" src={props.img} />
<h1 className="font-bold text-[8px] sm:text-[0.75rem]">
{props.name}
</h1>
</div>

<img src={arrow}    className="cursor-pointer  sm:w-[25px] w-[10px]"/>
    </div>
   ) 
}