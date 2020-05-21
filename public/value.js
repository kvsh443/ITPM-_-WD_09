// Need to write many post:action?.php files because can't pass the database names in .Tabledit-public 

// SIZE
$(document).ready(function() {
    $('#editable_tableS').Tabledit({
        url: 'actionS.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});
// Variable
$(document).ready(function() {
    $('#editable_tableV').Tabledit({
        url: 'actionV.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});

// Method
$(document).ready(function() {
    $('#editable_tableM').Tabledit({
        url: 'actionM.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});

// Inheritance
$(document).ready(function() {
    $('#editable_tableI').Tabledit({
        url: 'actionI.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});

// Coupling
$(document).ready(function() {
    $('#editable_tableC').Tabledit({
        url: 'actionC.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});

// Control Structures
$(document).ready(function() {
    $('#editable_tableT').Tabledit({
        url: 'actionT.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [2, 'value']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});

//Useless Last Table
$(document).ready(function() {
    $('#editable_tableL').Tabledit({
        url: 'actionL.php',
        deleteButton: false,
        saveButton: false,
        autoFocus: false,
        buttons: {
            edit: {
                class: 'btn btn-sm btn-primary',
                html: '<span class="glyphicon glyphicon-pencil"></span> &nbsp EDIT',
                action: 'edit'
            }
        },
        columns: {
            identifier: [0, "id"],
            editable: [
                [1, 'name'],
                [2, 'password']
            ]
        },
        restoreButton: false,
        onSuccess: function(data, textStatus, jqXHR) {
            console.log('onSuccess(data, textStatus, jqXHR)');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        },
        onFail: function(jqXHR, textStatus, errorThrown) {
            console.log('onFail(jqXHR, textStatus, errorThrown)');
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
        }
    });

});