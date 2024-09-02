/* eslint-disable react/prop-types */
import { useState } from "react";
import { SearchBar } from "./SearchBar";
import { Course } from "./Course";
import { CourseConnected } from "./CourseConnected";
import { Footer } from "./Footer";
import { sampleCourses } from "../data/data";
import { data } from "../data/data";
export const Search = (props) => {
    const [nbpage,setNbPage] =useState(1) ; 
    let [val,setValue]=useState("") ;
    function handleChange(e)
    {
     setValue(e.target.value);
    }
    const [filteredCourses, setFilteredCourses] = useState(sampleCourses);

 
    function HandleSearch(e) {
        e.preventDefault();
        const filtered = sampleCourses.filter((item) => {
            return (
                item.category.toLowerCase().includes(val.toLowerCase()) ||
                item.Duration.toLowerCase().includes(val.toLowerCase()) ||
                item.title.toLowerCase().includes(val.toLowerCase()) ||
                item.description.toLowerCase().includes(val.toLowerCase()) ||
                item.price.toLowerCase().includes(val.toLowerCase())
            );
        });
        console.log(filtered);
        setFilteredCourses(filtered);
        setNbPage(1); // Reset to first page after search
        console.log(val);
    }
      const categories = {
        Design: filteredCourses.filter(course => course.category === 'Design') ,
        Development: filteredCourses.filter(course => course.category === 'Development'),
        Marketing: filteredCourses.filter(course => course.category === 'Marketing'),
        Business: filteredCourses.filter(course => course.category === 'Business'),
        AllCategories: filteredCourses,
      };
    const style = `after:content-[''] font-bold relative cursor-pointer after:block after:bg-[rgb(32,180,134)] after:w-full after:h-[2px] sm:after:top-[39px] after:absolute after:bottom-0 text-[rgb(32,180,134)] after:top-[24px]`;
    const [cat, setCat] = useState("AllCategories");
    const getCourses = () =>{
        return categories[cat].slice((nbpage - 1) * 9, nbpage * 9) || []
    };
    
        
    const totalPages = categories[cat].length > 0 ? Math.ceil(categories[cat].length / 9) : 1;


    return (
        <div className="w-[90vw] mx-auto">
            <div className="flex list-none text-[#0A0A0A] justify-between text-[12px] sm:text-[14px] items-center">
                <li
                    className={cat === 'AllCategories' ? style : `cursor-pointer relative`}
                    onClick={() =>{ setCat("AllCategories") ,
                        setNbPage(1) ;

                    }}
                >
                    All categories
                </li>
                <li
                    className={cat === 'Design' ? style : `cursor-pointer relative`}
                    onClick={() => {setCat("Design") ,
                        setNbPage(1) ;
                    }}
                >
                    Design
                </li>
                <li
                    className={cat === 'Development' ? style : `cursor-pointer relative`}
                    onClick={() => {setCat("Development") , setNbPage(1) ;}}
                >
                    Development
                </li>
                <li
                    className={cat === 'Marketing' ? style : `cursor-pointer relative`}
                    onClick={() => {setCat("Marketing") , setNbPage(1) ;}}
                >
                    Marketing
                </li>
                <li
                    className={cat === 'Business' ? style : `cursor-pointer relative`}
                    onClick={() => {setCat("Business") , setNbPage(1) ;}}
                >
                    Business
                </li>
                <div className="sm:block hidden">
                    <SearchBar apply={true} />
                </div>
            </div>
            <hr className="h-[1px] w-full mb-10 mt-2 bg-black border-0"></hr>
            <div className="sm:hidden flex mb-10 justify-center w-[90vw] mx-auto">
            <form action="/search" className=" ">
        <div className="relative ">
            <input value={val} onChange={(e)=>{handleChange(e)}} type="text" name="q" className={ 'lg:w-[500px] md:w-[250px] pl-10 xs:w-[200px] w-[140px] outline-none p-4 rounded-[3px] md:h-[45px] h-[38px] placeholder:text-black md:placeholder:text-[14px] placeholder:text-[12px] font-medium sm:text-[14px] text-[12px] border border-black text-black bg-white' } placeholder="Search"/>
            <button onClick={HandleSearch} type="submit">
                <svg className={  'text-black md:h-4 md:w-4 x-3 h-3 top-[15px] absolute md:top-[15px]  left-2 fill-current ' } 
                    xmlns="http://www.w3.org/2000/svg" version="1.1"
                    x="0px" y="0px" viewBox="0 0 56.966 56.966"
                  >
                    <path
                        d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z">
                    </path>
                </svg>
            </button>
        </div>
    </form>            </div>
            <div className="grid my-10 grid-cols-2 gap-2 sm:grid-cols-3 sm:gap-4 items-center">
  {
    !props.yes ?
 (    getCourses().lentgh!= 0 ?
  (  getCourses().map((item) => {
      return (
        <Course 
          rating={item.rating} 
          ratingSrc={item.ratingPic} 
          key={item.id} 
          src={item.src} 
          category={item.category} 
          Duration={item.Duration} 
          title={item.title} 
          description={item.description} 
          price={item.price} 
          Constructor={item.Constructor} 
          photo={item.photo} 
        />
      );
    })) : "") : (  getCourses().map((item,index) => {
        return (
          <CourseConnected key={item.id} src={item.src} category={item.category} Duration={item.Duration} title={item.title} description={item.description} price={item.price} Constructor={item.Constructor}  photo={item.photo} number={index+1} total={data.length}  
          />
        );
      }))
  }

</div>
<div className="flex mb-20 justify-end space-x-4">
<button className={nbpage == 1 ? "bg-[#20b486]/30 w-[40px] h-[40px] font-bold text-white" : "bg-[#20b486] w-[40px] h-[40px] font-bold text-white"}  onClick={()=>
            {
                console.log(nbpage);
                nbpage != 1 ?setNbPage(nbpage -1) : ""
                
            }
        } >
{"<"}
        </button>
        <button  className={nbpage == totalPages ?  "bg-[#20b486]/30 w-[40px] h-[40px] font-bold text-white" : "bg-[#20b486] w-[40px] h-[40px] font-bold text-white"}  onClick={()=>
            {
                nbpage != totalPages ?setNbPage(nbpage +1) : "" ;
                console.log(nbpage);
            }
        } >
{">"}
        </button>
     

    </div>
      <Footer/>
        </div>
    );
}
