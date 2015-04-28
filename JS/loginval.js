$(document).ready(function () {
        $('#loginform').isHappy({
          fields: {
            // reference the field you're talking about, probably by `id`
            // but you could certainly do $('[name=name]') as well.
            '#username': {
              required: true,
              message: 'Might we inquire your name'
            },
            '#password': {
              required: true,
              message: 'Dont forget your password'
            }
          }
        });
      });