/* eslint-disable no-unused-vars */
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { data } from "../data/data";
import { useEffect } from "react";
import { useState } from "react";
import { CourseConnected } from "./CourseConnected";
export const SlideConnected=(props)=>
{
   const [nb,setNb]=useState(3);

   // the function that returns the numer of lessons for a given user 
   const getNbLessons=()=>
   {
    return 7 ;
   }
   var settings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 3,
    initialSlide: 0,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          initialSlide: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  };
      useEffect(()=>
    {
        window.addEventListener("resize",()=>
        {
            window.innerWidth<=640 ? setNb(2) :setNb(3);

        })
    },[]);
      return (
<div className="mt-20 mx-auto w-[90vw]">
<Slider {...settings}>
         {
              data.map((item,index)=>
              { 
                  return <CourseConnected key={item.id} src={item.src} category={item.category} Duration={item.Duration} title={item.title} description={item.description} price={item.price} Constructor={item.Constructor}  photo={item.photo} number={index+1} total={getNbLessons()} />;
              })
          }  
        </Slider>
</div>


       
      );
}