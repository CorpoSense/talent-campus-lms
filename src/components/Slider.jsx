import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { Course } from "./Course";
import { data } from "../data/data";
import { useEffect } from "react";
import { useState } from "react";
export const Slide=()=>
{
   const [nb,setNb]=useState(3);

    var settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: nb,
        slidesToScroll: 3,
        
      };
      useEffect(()=>
    {
        window.addEventListener("resize",()=>
        {
            window.innerWidth<=640 ? setNb(2) :setNb(3);

        })
    },[]);
      return (

        <Slider {...settings}>
         {
              data.map((item)=>
              { 
                  return <Course key={item.id} src={item.src} category={item.category} Duration={item.Duration} title={item.title} description={item.description} price={item.price} Constructor={item.Constructor} photo={item.photo} />;
              })
          }  
        </Slider>
      );
}