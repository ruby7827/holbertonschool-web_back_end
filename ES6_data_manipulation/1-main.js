// eslint-disable-next-line import/extensions
import getListStudentIds from './1-get_list_student_ids.js';
// eslint-disable-next-line import/extensions
import getListStudents from './0-get_list_students.js';

console.log(getListStudentIds('hello'));
console.log(getListStudentIds(getListStudents()));
