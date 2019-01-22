

function addDays(theDate, days) {
    return new Date(theDate.getTime() + days * 24 * 60 * 60 * 1000);
}

$(document).ready(function () {

    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 200, // Creates a dropdown of 15 years to control year
        format: 'yyyy-mm-dd', //%Y-%m-%d
        //min: new Date(),
        //max: addDays(new Date(), 1),
        closeOnSelect: true,
        onSet: function (context) {
            if (context.select !== undefined) {
                this.close();
            }
        }
    });

    file_input = $('.file-input');
    file_input.wrap('<div class = "file-field input-field"><div class = "btn"></div></div>');
    $("<span>Browse</span>").insertBefore(file_input);
    $("<div class = \"file-path-wrapper\">\n" +
        "                     <input class = \"file-path validate\" type = \"text\"\n" +
        "                        placeholder = \"Upload file\" />\n" +
        "                  </div>").insertAfter(file_input.parent());


    $("[for=id_form-0-attached_piece]").remove()
    $("[for=id_attached_piece]").remove()

    $(document).on('DOMNodeInserted', function (e) {
        if ($(e.target).hasClass('link-formset')) {
            //console.log($(e.target)[0])
            $($(e.target)[0]).find('div > p:nth-child(3)').contents().filter(function () {
                return this.nodeType === 3 || this.localName === 'a';
            }).remove();
            $($(e.target)[0]).find('div.error-form').remove();

        }
    });


    $('select').removeAttr('required')


    is_staff_input = $("#id_is_staff")
    if (is_staff_input.length > 0) {
        if (is_staff_input.attr("create-form") === "yes") {
            $('label[for="' + is_staff_input.attr('id') + '"]').css({
                'padding-bottom': '36px'
            });
        }
    }
    edit_password = $("#id_edit_password")
    if (edit_password.length > 0) {
        password_input = $("#id_password");
        confirm_password_input = $("#id_confirm_password");
        if (!edit_password.is(":checked")) {
            password_input.attr('disabled', true)
            password_input.parent().hide()
            confirm_password_input.attr('disabled', true)
            confirm_password_input.parent().hide()
        }

        edit_password.change(function () {
            if (this.checked) {
                password_input.attr('disabled', false)
                password_input.parent().show()
                confirm_password_input.attr('disabled', false)
                confirm_password_input.parent().show()
            } else {
                password_input.attr('disabled', true)
                password_input.parent().hide()
                confirm_password_input.attr('disabled', true)
                confirm_password_input.parent().hide()
            }
        })
    }
    $(':input[required]').attr('required', false)

    $("ul.tabs > li.tab > a").unbind('click');

    $('.modal-trigger').leanModal();

    $(".collapsible-header").click(function () {
        $(".more", this).toggle()
        $(".less", this).toggle()
    });

    // youssef modifs
    $("#id_start_time").parent(".input-field").addClass("clockpicker");
    $("#id_end_time").parent(".input-field").addClass("clockpicker");
    $('.clockpicker').clockpicker({
        donetext : 'Done',
        'default' : 'now'
    });
})

$(document).on('ready', function () {
    $('.link-formset').formset({
        addText: 'Add Attached piece',
        deleteText: 'Remove Attached piece'
    });
});
