import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const roomSizes = [19, 20, 34];

  const rooms = [];
  for (const roomSize of roomSizes) {
    rooms.push(new ClassRoom(roomSize));
  }
  return rooms;
}
