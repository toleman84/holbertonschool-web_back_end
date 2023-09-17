import ClassRoom from './0-classroom';

function initializeRooms() {
  const roomSizes = [19, 20, 34];
  const room = [];
  for (const roomSize of roomSizes) {
    rooms.push(new ClassRoom(roomSize));
  }
  return rooms;
}
