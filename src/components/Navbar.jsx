/* eslint-disable no-unused-vars */
import { BrowserRouter as Router, Link } from 'react-router-dom';
import { SearchBar } from './SearchBar';
import { useEffect, useState } from 'react';
import algiers from '../../public/algiers.png';
import menu from '../../public/menu.svg';
import close from '../../public/close.svg'
import out from '../../public/out.svg'
export const Navbar=()=>
{
  const [visible,setVisible]=useState(false);
  const [isConnected , setIsconnected]=useState(false);
  const handleToggle=()=>
  {
visible == false ? setVisible(true) : setVisible(false);
  }
  const getEmailUsername=()=>
  {
    return ["Bendahmene Nesrine" , "ln_bendahmane@esi.@dz"]
  }
  const goToProfile=()=>
    {

    }  
  const goToLearning=()=>
  {

  }
  const logOut=()=>
  {

  }
  const onResize = () => {
    window.innerWidth >= 640 ? setVisible(false) : ""
  };

  useEffect(() => {
    onResize(); 
    window.addEventListener('resize', onResize);
    return () => {
      window.removeEventListener('resize', onResize);
    };
  }, []);

    return (

          <div className='sticky'>
          <div className='w-full z-50 bg-white py-2 border border-x-0 border-b-1'>
          <div className="sticky  h-[50px] items-center flex justify-between  w-[90%] mx-auto  ">
         <h3 className='text-[18px]'> <span className='text-[#ffc107] font-bold italic'>Talent</span>  <span className='text-[#20b486] italic font-bold'>Campus
          </span> </h3>
         <SearchBar/>
       { !visible &&  <img className='sm:hidden h-8 cursor-pointer  block' src={menu} onClick={handleToggle} />}
        {visible && <img className='sm:hidden h-8 cursor-pointer  block' src={close} onClick={handleToggle} />}
         <div className="sm:grid font-medium hidden grid-cols-2 divide-x">
              <ul className=" text-[#6D737A]  text-[12px] items-center hidden sm:flex justify-between b-sm:justify-around
               space-x-3 mr-2">
                <li> <a href="#Home">Home</a> </li>
                <li><a href="#Courses">Courses</a> </li>
                {isConnected && <li visibility={isConnected} className='cursor-pointer' onClick={goToLearning}> My learning </li>}
                <li><a href="#Contact">Contact</a></li>
             </ul>
            { isConnected ? <img src={algiers} onClick={goToProfile} className='w-[37px] cursor-pointer h-[37px] rounded-full ml-auto'/> :
            (<ul className="flex items-center justify-end space-x-2 text-[12px]">
              <li>
                  <button className=' text-[#6D737A] text-[12px]' >   <Link to="./Login"> Login </Link>
                  </button>
              </li>
              <li className=''>
                   <button className="bg-[#20b486] text-center text-white  font-medium font-['public Sans'] sm:w-[85px] w-[60px] leading-normal px-[15px] py-[8px] rounded-[2px]"><Link to="./Signup"> Sign up </Link></button>
              </li>
          
            </ul>) }
          </div>
     </div>
     </div>
   {visible && !isConnected &&  <ul className="w-full bg-white z-50 absolute font-medium text-[#6D737A] text-[14px] flex-col items-center justify-center space-y-6 h-[350px]">
                <li className='text-center mt-[50px]'> <a href="#Home">Home</a> </li>
                <li className='text-center'><a href="#Courses">Courses</a> </li>
                {isConnected && <li visibility={isConnected} className='cursor-pointer' onClick={goToLearning}> Mylearning </li>}
                <li className='text-center'><a href="#Contact">Contact</a></li>
                <li className='w-8 mx-auto '>
                  <button className=' mx-auto text-center ' >   <Link to="./Login">Login </Link>
                  </button>
              </li>
              <li className='w-[120px] mx-auto '>
                   <button className="bg-[#20b486] text-center mx-auto text-white  font-medium w-full font-['public Sans'] leading-normal px-[10px] py-[8px] rounded-[2px]"><Link to="./Signup"> Sign up </Link></button>
              </li>
             </ul>}


{/* WHEN THE USER IS CONNECTED HOW DOES THE NAVBAR LOOKS ON THE PHONE */}
             {visible && isConnected &&  
             <div className='mt-4 bg-white z-50 absolute w-[90%] mx-auto'>
               <div className='mx-auto space-x-6 flex '>
                 <img src={algiers} className='rounded-full w-[80px] h-[80px] ' alt="Profile picture"/> 
                 <div className='flex-col flex items-left justify-center'>
                  <h1 className='font-semibold text-[17px]'>
                    {getEmailUsername()[0]}
                  </h1>
                  <h1 className='text-[12px] font-medium text-[#343a40] text-left'>
                    {getEmailUsername()[1]}
                    </h1>
               </div>
             </div> 
             <hr className='my-4'></hr>
             <ul className='space-y-2'>
              <li className='text-left  text-[13px]'> <a href="#Home">Home</a> </li>
                <li className='text-left text-[13px]'><a href="#Courses">Courses</a> </li>
                <li className='text-left text-[13px]'><a href="#Contact">Contact</a></li>
             </ul>
             <hr className='my-4'></hr>
             <ul className='space-y-2'>
             <li className='text-left text-[13px] cursor-pointer'> My learning </li>
                <li className='text-left text-[13px] cursor-pointer'>My cart </li>
                <li className='text-left text-[13px] cursor-pointer'>My favorites</li>
                <li className='text-left text-[13px] cursor-pointer'>Notifications</li>
             </ul>
             <hr className='my-4'></hr>
             <ul className='space-y-2'>
             <li className='text-left text-[13px] cursor-pointer'> Language </li>
                <li className='text-left text-[13px] cursor-pointer'>Settings </li>
                <li className='text-left text-[13px] cursor-pointer'>Help and support</li>
             </ul>
             <hr className='my-4'></hr>
             <div className='flex items-center space-x-2'>
            <button onClick={logOut}><img src={out}/></button>  
              <h1  className='font-bold text-[#F13C3C] text-[13px]'>
              <button onClick={logOut}>Log out</button>  
              </h1>
              </div> 
             </div>
             }
          </div>
    
    
    )
}