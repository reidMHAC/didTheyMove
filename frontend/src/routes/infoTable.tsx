import React, { useEffect, useState } from 'react';
import axios from "axios";
import { Link } from 'react-router-dom';



export default function InfoTable() {
    const [customerData, setCustomerData] = useState<any>(null);

    const getInfo = () => {
        fetch('/api/didTheyMove')
            .then(res => res.json())
            .then(
                (result) => {
                // whatever you want to do with the list of employees will happen here
                if(result.length > 0) {
                    setCustomerData(result);
                }
                
                },
                (error) => {
                    console.log(error);  // error handling
                }
            )
    };

    const checkMoved = () => {
        fetch('/api/checkMoved/JB/')
    };

    useEffect(() => getInfo(), []);

	return (
        <>
            <h1>
                Customer Info
            </h1>
            <Link to='/'>
                <button style={{cursor:'pointer'}} className='p-btn p-prim-col'>Upload CSV</button>
            </Link>
            <button style={{cursor:'pointer'}} onClick={checkMoved} className='p-btn p-prim-col'>Check Moved Status</button>
            {customerData ? (
                <>
                <table>
                    <tbody>
                        
                        <tr>
                            <th>Customer</th>
                            <th>Address</th>
                            <th>Date</th>
                            <th>Phone Number</th>
                            <th>Moving Status</th>
                        </tr>
                        {customerData.map((customer:any, index:number) => {
                            return(
                                <tr key={index}>
                                    <td>{customer.customer}</td>
                                    <td>{customer.address}</td>
                                    <td>{customer.zipCode}</td>
                                    <td>{customer.phoneNumber}</td>
                                    <td>{customer.status}</td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
                </>
            ):(
                <h1>No Data Available</h1>
            )}
        </>
	);
}


