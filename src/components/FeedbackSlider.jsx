import { Feedback } from "./Feedback"
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { useState ,useEffect } from "react";
import { Feedbacks } from "../data/data";

export const FeedbackSlider=()=>
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
              Feedbacks.map((item)=>
              { 
                  return <Feedback key={item.id} img={item.img} name={item.name} profession={item.profession} details={item.details}  />;
              })
          }  
        </Slider>
      );
}