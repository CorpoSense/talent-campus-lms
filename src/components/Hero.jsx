import hat from "/hat.svg";
import wifi from "/wifi.svg";
import curvedLine from "/curvedLine.svg";
import cloud from "/cloud.svg";
import star from "/star.svg";

export const Hero=()=>
    {
        return (
        <div className="w-[90%] z-10 mx-auto  remaining-height-element items-center justify-center  flex flex-col  space-y-5">
          <div className="md:w-[800px] z-10 w-[500px] top-[67px]  right-0 absolute bgHome remaining-height-element ">
          </div>
          <img src={hat} className="absolute z-10 xxs:w-[100px] xxs:top-[15%] w-[50px] top-[17%] right-[10%] lg:right-[30%] md:right-[20%]" ></img>
          <img src={wifi} className="absolute w-[20px] sm:w-[30px] top-[20%] left-[10%] lg:left-[30%] md:left-[20%]" ></img>
          <img src={star} className="absolute w-[20px] sm:w-[30px] top-[12%] left-[3%] lg:left-[20%] md:left-[15%]" ></img>
          <img src={curvedLine} className="xxs:absolute hidden xxs:w-[100px] xxs:bottom-[15%] w-[50px] bottom-[10%] right-[7%] lg:right-[25%] md:right-[15%]" ></img>
          <img src={curvedLine} className="absolute  xxs:w-[100px] xxs:bottom-[10%] w-[50px] bottom-[7%] right-0" ></img>
          <img src={cloud} className="absolute xxs:w-[70px] sm:w-[100px] xxs:bottom-[10%] w-[50px] bottom-[7%] left-0" ></img>
          
   <h1 className="sm:text-5xl z-10 text-4xl z-20 leading-[50px] sm:leading-[70px] font-bold text-center" > <span className=" bg-gradient-to-r from-[#007bff] to-[rgb(32,180,134)]    inline-block text-transparent bg-clip-text ">
      
          Shaping  </span> your future <br></br> with the skills that matter </h1>
       
          <p className="text-center z-20">
          Talent Campus is an interesting platform <br></br>
          that will teach you in more an interactive way
          </p>
          <button className=" sm:w-[200px] w-[150px]  bg-[#20b486]  justify-center  text-white rounded-[2px] px-[10px] py-[10px] sm:py-[15px]  items-center">
            Let&apos;s start
          </button>
            </div>
        )
    }