/* eslint-disable react/prop-types */
export const Input=(props)=>
{
    return <>
   <label className="text-[#202121]/80 text-[14px]" htmlFor={props.id}>
            {props.label}
           </label>
             <input className="border text-[#202121]/80 xxs:w-[300px] w-[200px] lg:w-[400px] placeholder:text-[13px]  rounded-[2px] focus:outline-none text-[12px] px-4 py-2" 
            id={props.id} 
            type={props.type}  
            label={props.label}
            name={props.name}
            value={props.value}
            onChange={props.onChange}
            placeholder={props.placeholder}
             /></>}