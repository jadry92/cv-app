
export interface IContact {
    name: string;
    email: string;
    phone: string;
    location: string;
    linkedin: string;
    website: string;
    github: string;
}

export interface IExperience {
    role: string;
    company: string;
    startDate: string;
    endDate: string;
    description: string;
}


export interface IProject {
    title: string;
    url: string;
    description: string;
    techStack: string[];  
}

export interface IEducation {
    degree: string;
    school: string;
    startDate: string;
    endDate: string;
    description: string;
}

export interface ISkill {
    name: string;
    level: string;
}

export interface Idata {
    contact: IContact;
    about: string;
    experience: IExperience[];
    education: IEducation[];
    projects: IProject[];
    skills: ISkill[];
}
