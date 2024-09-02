/* eslint-disable react/prop-types */
export const Course =(props)=>
{
     return (
        <div className=" shadow rounded-[8px] w-[90%] bg-white space-y-4  py-3 items-center flex flex-col">
          <img className="rounded-[8px] w-[90%]" src={props.src}/>
          <div className="flex md:text-[15px] flex-row  text-[#343A4099] w-[90%] text-[10px] space-x-3 justify-between">
            <h1>
    { props.category}            
            </h1>
<h1>
{props.Duration}    
</h1>

          </div>
          <h1 className="md:text-lg w-[90%] text-[12px] font-bold">
         { props.title}
          </h1>
          <p className="w-[90%] text-[10px] md:text-[12px] text-[#343A4099]">
           {props.description} 
          </p>
          <div className="flex md:text-[15px] flex-row  text-[#343A4099] w-[90%] text-[10px] space-x-3 justify-between items-center">
           
                <div className="flex space-x-1 items-center justify-between">
                <img className="sm:w-[30px] w-[25px] cursor-pointer" src={ props.photo} />  
 
                    <h1 className="sm:text-[12px] text-[10px] text-black font-bold">
                    { props.Constructor}
                    </h1>     
                </div>
<h1 className="text-[#007BFF]">
{props.price}    
</h1>


          </div> 
          <div className="flex w-[90%] justify-start space-x-2 ">
<h1 className="sm:text-[12px] text-[10px] text-black font-bold">
                    { props.rating}
                    </h1>  
                    <img className="w-[90px]" src={props.ratingSrc} /> 
</div>
        </div>
     )
}