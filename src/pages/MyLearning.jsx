import { Navbar } from "../components/Navbar"
import { Search } from "../components/Search"
export const MyLearning=()=>
{
    return (
        <div className="w-[100vw]">
                        <Navbar/>  

<div className="w-[90vw] mx-auto">
        <h1 className="md:text-5xl text-[rgb(0,123,255)] text-xl sm:text-2xl tracking-wide text-left mt-10 font-bold mb-10">
My Learning
            </h1> 
            <Search yes={true}/>
        </div>
        </div>
        
    )
}