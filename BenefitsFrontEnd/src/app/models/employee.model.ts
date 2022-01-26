import { Dependent } from "./dependent.model";

export class Employee {
    firstName: string;
    middleName?: string;
    lastName: string;
    dependents: Dependent[];
}