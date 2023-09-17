import { IContact } from "../interfaces";


export default function ContactInfo({name, email, phone, location, linkedin, website}: IContact) {
  return (
    <>
        <h1>{name}</h1>
        <p>{email}</p>
        <p>{phone}</p>
        <p>{location}</p>
        <p>{linkedin}</p>
        <p>{website}</p>
    </>
  )
}