#!/usr/bin/node
module.exports = class square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
