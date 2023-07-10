$(document).ready(function() {
    // Инициализация перетаскивания элементов с помощью Dragula
    dragula([
        document.getElementById('todo-column'),
        document.getElementById('inprogress-column'),
        document.getElementById('done-column')
    ]).on('dragend', function(el) {
        updateTaskStatus($(el));
    });
  
    // Инициализация перетаскивания элементов с помощью jQuery UI
    $('.column').sortable({
        connectWith: '.column',
        stop: function(event, ui) {
            var task_id = ui.item.data('task-id');
            var status = ui.item.closest('.column').attr('id');
            $.ajax({
                url: 'update_task_status/',
                type: 'POST',
                data: {
                    'task_id': task_id,
                    'status': status
                },
                success: function(response) {
                    console.log(response);
                },
                error: function(response) {
                    console.log(response);
                }
            });
        }
    });
    
    function updateTaskStatus(taskElement) {
        var taskId = taskElement.data('task-id');
        var newStatus = taskElement.closest('.column').attr('id');
  
        $.ajax({
            url: 'update_task_status/',
            type: 'POST',
            data: {
                'task_id': taskId,
                'status': newStatus
            },
            success: function(response) {
                console.log('Task status updated successfully.');
            },
            error: function(xhr, status, error) {
                console.error('Error updating task status:', error);
            }
        });
    }
});
