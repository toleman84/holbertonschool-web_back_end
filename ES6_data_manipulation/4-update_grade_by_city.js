export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);

  const updatedStudents = filteredStudents.map((student) => {
    const newGrade = newGrades.find((grade) => grade.studentId === student.id);
    const updatedStudent = { ...student };
    updatedStudent.grade = newGrade ? newGrade.grade : 'N/A';
    return updatedStudent;
  });

  return updatedStudents;
}
