import React from 'react'

export default function index() {
    let names = 'Тимур'
    const user = {
        firstNAme: 'Тимур',
        lastName: 'Расуев'
    }
  return (
    <>
    <div>{user.firstNAme}</div>
    <div>{user.lastName}</div>
    
    </>
  )
}
