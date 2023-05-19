import Mock from 'mockjs';

Mock.mock('/api/recommendations', 'get', {
  'list|10': [
   {
      'id|+1': 1,
      'title': '@ctitle(5,20)',
      'description': '@cparagraph(1,2)',
      'score|2-5': 0,
      'image': Mock.Random.image('200x200', '#FFC107', '#FFF', 'Mock.js'),
    },
  ],
});