export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);

  const updatedStudents = filteredStudents.map((student) => {
    const newGrade = newGrades.find((grade) => grade.studentId === student.id);
    student.grade = newGrade ? newGrade.grade : 'N/A';
    return student;
  });

  return updatedStudents;
}
