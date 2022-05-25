config1 = {
    # As yet unitless
    'gravity': 20,
    # Window size
    'extent': 100,
    # The time step in milliseconds, used by the System's update function and by FuncAnimation
    'time_step': 30,
    'particles': {
        'sun': {
            # Initial position
            'p_0': [0, 0],
            # Initial velocity
            'v_0': [0, 0],
            # Not used if forces are calculated from other bodies.
            'a': [0, 0],
            # Unitless
            'm': 1.0e1,
            # Plotting color for the particle's circle and tracer.
            'color': 'orange'
        },
        'earth': {
            'p_0': [0, 20],
            'v_0': [-20, 0],
            'a': [0, -5],
            'm': 10.0,
            'color': 'blue',
            'time_step': 100,
            'window': ((-10, 10), (-10, 10)),
        },
        'mars': {
            'p_0': [30, 0],
            'v_0': [20, 0],
            'a': [0, -5],
            'm': 10.0,
            'color': 'brown',
        },
    }
}

config2 = {
    'gravity': 1,
    'extent': 100,
    'time_step': 30,
    'particles': {
        'sun': {
            'p_0': [0, 0],
            'v_0': [0, 0],
            'a': [0, 0],
            'm': 1.0e2,
            'color': 'orange'
        },
        'earth': {
            'p_0': [50, 0],
            'v_0': [0, 6.3245],
            'a': [0, -5],
            'm': 10.0,
            'color': 'blue',
            'time_step': 100,
            'window': ((-10, 10), (-10, 10)),
        },
        'mars': {
            'p_0': [-70, 0],
            'v_0': [0, 5.34522],
            'a': [0, -5],
            'm': 10.0,
            'color': 'brown',
        },
    }
}


config3 = {
    'gravity': 200,
    'extent': 1000,
    'time_step': 30,
    'particles': {
        'sun': {
            'p_0': [0, 0],
            'v_0': [0, 0],
            'a': [0, 0],
            'm': 1.0e2,
            'color': 'orange'
        },
        'earth': {
            'p_0': [0, 200],
            'v_0': [30, 0],
            'a': [0, -5],
            'm': 10.0,
            'color': 'blue',
            'time_step': 100,
            'window': ((-10, 10), (-10, 10)),
        },
        'mars': {
            'p_0': [200, 0],
            'v_0': [0, -30],
            'a': [0, -5],
            'm': 10.0,
            'color': 'brown',
        },
        'venus': {
            'p_0': [0, -200],
            'v_0': [-30, 0],
            'a': [0, 0],
            'm': 10.0,
            'color': 'orange'
        },
        'mercury': {
            'p_0': [-200, 0],
            'v_0': [0, 30],
            'a': [0, -5],
            'm': 20.0,
            'color': 'green',
            'time_step': 100,
            'window': ((-10, 10), (-10, 10)),
        },
        'saturn': {
            'p_0': [-400, 500],
            'v_0': [20, -20],
            'a': [0, -5],
            'm': 10.0,
            'color': 'purple',
        },
        'jupiter': {
            'p_0': [400, -500],
            'v_0': [-10, 5],
            'a': [0, -5],
            'm': 10.0,
            'color': 'pink',
        },
    }
}
