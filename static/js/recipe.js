// Dynamic functionality was inspired by fellow student Nicola from their project 'Sustain Eat' 
//  https://github.com/Nicola2309/MS3

$(document).ready(function () {

    // Declare Variables
    var max_ingredients = 30;
    var ingredient_row = $(".ingredient-row");
    var add_ingredient = $(".add-ing-btn");
    var ingredient = 1;

    var max_directions = 30;
    var direction_row = $(".direction-row");
    var add_direction = $(".add-dir-btn");
    var direction = 1;

    /* -----------------------
        create_recipe.html 
    ----------------------- */
    // Append New Ingredient
    $(add_ingredient).click(function (e) {
        e.preventDefault();
        if (ingredient < max_ingredients) {
            ingredient++;
            $(ingredient_row).append('<div class="col-12 form-group ing-input"><input id="ingredients" class="form-control" type="text" name="ingredients"/><label for="ingredients" required></label><a href="#" class="remove_field">Delete</a></div>');
        }
    });

    // Delete New Ingredient
    $(ingredient_row).on("click", ".remove_field", function (e) {
        e.preventDefault();
        $(this).parent('div').remove();
        ingredient--;
    });

    // Append New Direction
    $(add_direction).click(function (e) {
        e.preventDefault();
        if (direction < max_directions) {
            direction++;
            $(direction_row).append('<div class="col-12 form-group dir-input"><textarea id="directions" class="form-control" type="text" name="directions" maxlength="300" rows="1" required/></textarea><label for="directions"></label><a href="#" class="remove_field">Delete</a></div>')
        }
    });

    // Delete New Direction
    $(direction_row).on("click", ".remove_field", function (e) {
        e.preventDefault();
        $(this).parent('div').remove();
        direction--;
    });

    /* -----------------------
        edit_recipe.html 
    ----------------------- */

});