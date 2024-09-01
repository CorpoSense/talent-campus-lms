export const CourseConnected =(props)=>
{
    const getProgress =()=>
    {
        return 60 ;
    }
    return (
        <div className=" shadow rounded-[8px]  bg-white space-y-4  py-3 items-center flex flex-col">
          <img className="rounded-[8px] w-[90%]" src={props.src}/>
         
          <h1 className="md:text-lg w-[90%] text-[12px] font-bold">
         { props.title}
          </h1>
          <div className="flex md:text-[15px] flex-row  text-[#343A4099] w-[90%] text-[10px] space-x-3 justify-between items-center">
           
                <div className="flex space-x-1 items-center justify-between">
                <img className="sm:w-[30px] w-[25px] cursor-pointer" src={ props.photo} />  
 
                    <h1 className="sm:text-[12px] text-[10px] text-black font-bold">
                    { props.Constructor}
                    </h1>     
                </div>


          </div> 
          <progress className="w-[90%] h-2 [&::-webkit-progress-bar]:rounded-lg [&::-webkit-progress-value]:rounded-lg   [&::-webkit-progress-bar]:bg-slate-300 [&::-webkit-progress-value]:bg-[#FFC107] [&::-moz-progress-bar]:bg-[#343A40] mx-auto" id="file" value={getProgress()} max="100"> 32% </progress>
          <h1 className="font-bold text-right w-[90%] text-black/50 text-[13px]">
            lesson {props.number} of {props.total}
          </h1>
        </div>
     )
}