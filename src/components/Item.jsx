/* eslint-disable react/prop-types */
export const Item=(props)=>
{
    return (
        <div className="flex space-x-1 items-center ">
            <img className="sm:w-[50px] xxs:w-[40px] w-[25px] " src={props.src}>
            </img>
            <div className="flex  flex-col">
               <h1 className="font-bold text-[8px] sm:text-[12px]">
                {props.nb}
            </h1>
            <p className="text-[#52565c] text-[8px] sm:text-[12px]">
                {props.name} +
            </p>
  
            </div>
           
        </div>
    )
}