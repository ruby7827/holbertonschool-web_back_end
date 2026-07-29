// eslint-disable-next-line import/extensions
import getListStudents from './0-get_list_students.js';
// eslint-disable-next-line import/extensions
import getStudentIdsSum from './3-get_ids_sum.js';

const students = getListStudents();
const value = getStudentIdsSum(students);

console.log(value);
