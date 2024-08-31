import React from 'react';
import { AdminNavbar } from '../components/AdminNavbar';
import { Line, Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend, BarController } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend);

const topCourses = [
  { name: 'Python for Beginners', enrollments: '3,200', avgTimeSpent: '1.5 hours/session', avgRating: '4.8/5' },
  { name: 'Digital Marketing', enrollments: '2,900', avgTimeSpent: '1.2 hours/session', avgRating: '4.7/5' },
  { name: 'Introduction to Data Science', enrollments: '3,500', avgTimeSpent: '2 hours/session', avgRating: '4.8/5' },
  { name: 'Graphic Design Masterclass', enrollments: '2,500', avgTimeSpent: '1.3 hours/session', avgRating: '4.6/5' },
  { name: 'Business Analytics', enrollments: '2,450', avgTimeSpent: '1.3 hours/session', avgRating: '4.7/5' },
];

const lineData = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  datasets: [{
    label: 'Total Student Enrollments',
    data: [100, 200, 150, 400, 300, 500, 400, 350, 450, 500, 600, 700],
    borderColor: '#36A2EB',
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    fill: true,
  }],
};

const barData = {
  labels: ['Business', 'Design', 'Computer Science', 'Economics', 'Marketing', 'Data Science'],
  datasets: [{
    label: 'Course Performance by Category',
    data: [80, 90, 70, 60, 75, 85],
    backgroundColor: '#4BC0C0',
    barThickness: 10, // Adjust thickness of bars
  }],
};

const completionData = {
  labels: ['Python for Beginners', 'Business Analytics', 'Introduction to Data Science', 'Graphic Design Masterclass', 'Digital Marketing'],
  datasets: [{
    label: 'Completion Rate',
    data: [60, 70, 80, 75, 30],
    backgroundColor: ['#F9A602', '#F9A602', '#4BC0C0', '#4BC0C0', '#F9A602'],
    borderRadius: 5,
    borderSkipped: false,
    barThickness: 10, // Reduce the thickness of bars
  }],
};

const options = {
  indexAxis: 'y',
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: (context) => `${context.raw}%`,
      },
    },
  },
  scales: {
    x: {
      beginAtZero: true,
      ticks: {
        stepSize: 10,
        callback: (value) => `${value}%`,
      },
    },
    y: {
      grid: {
        display: false,
      },
      barPercentage: 0.5, // Adjust the space between bars
      categoryPercentage: 0.5, // Adjust the space between categories
    },
  },
};

export const AdminStatistics = () => {
  return (
    <>
      <AdminNavbar />
      <div className="min-h-[100vh] mx-auto w-[90%]">
        <h1 className="text-4xl tracking-wide font-bold mt-10 text-gradient">Analytics Dashboard</h1>
        <div className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-10">
          {/* Total Student Enrollments Chart */}
          <div className="bg-white shadow-md rounded-lg p-6 h-[500px] flex flex-col">
            <h2 className="text-2xl mb-4">Total Student Enrollments</h2>
            <div className="flex-grow">
              <Line data={lineData} options={{ maintainAspectRatio: false }} />
            </div>
          </div>
          {/* Course Performance by Category Chart */}
          <div className="bg-white shadow-md rounded-lg p-6 h-[500px] flex flex-col">
            <h2 className="text-2xl mb-4">Course Performance by Category</h2>
            <div className="flex-grow flex items-center justify-end">
              <Bar data={barData} options={{ maintainAspectRatio: false }} />
            </div>
          </div>
        </div>
        {/* Top Courses by Enrollment and Course Completion Rates */}
        <div className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-10">
          {/* Top Courses by Enrollment Table */}
          <div className="bg-white shadow-md rounded-lg p-6 flex flex-col h-[400px]">
            <h2 className="text-2xl mb-4 ">Top Courses by Enrollment</h2>
            <div className="overflow-x-auto">
            <table className="min-w-full text-left bg-gray-50 border-separate border-spacing-0">
  <thead className="bg-[#F7FAFC] text-[#A0AEC0]">
    <tr>
      <th className="py-2 text-center border-b border-gray-200">Course Name</th>
      <th className="py-2 text-center border-b border-gray-200">Enrollments</th>
      <th className="py-2 text-center border-b border-gray-200">Avg. Time Spent</th>
      <th className="py-2 text-center border-b border-gray-200">Avg. Rating</th>
    </tr>
  </thead>
  <tbody className="text-[#718096]">
    {topCourses.map((course, index) => (
      <tr key={index} className={`border-b border-gray-200 ${index % 2 === 0 ? 'bg-gray-100' : 'bg-gray-50'}`}>
        <td className="py-2 w-[150px] overflow-hidden whitespace-normal text-center">{course.name}</td>
        <td className="py-2 text-center">{course.enrollments}</td>
        <td className="py-2 text-center">{course.avgTimeSpent}</td>
        <td className="py-2 text-center">{course.avgRating}</td>
      </tr>
    ))}
  </tbody>
</table>



            </div>
          </div>
          {/* Course Completion Rates Chart */}
          <div className="bg-white shadow-md rounded-lg p-2 flex flex-col h-[400px] mb-10 ">
            <h2 className="text-2xl mb-4 mt-6 ml-6">Course Completion Rates</h2>
            <div className="flex-grow flex items-center justify-start">
              <Bar data={completionData} options={options} />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
